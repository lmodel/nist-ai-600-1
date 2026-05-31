"""Verify that the LinkML schemas reflect the SSSOM mapping TSV files.

The SSSOM TSV files under ``src/<schema-name>/mappings/`` are the
authoritative source of cross-vocabulary mappings. This script reads
them and confirms that the corresponding ``exact_mappings`` /
``close_mappings`` / ``broad_mappings`` / ``narrow_mappings`` /
``related_mappings`` fields are present on the matching elements in
the LinkML schemas at ``src/<schema-name>/schema/``.

This is a *verifier* (read-only) so that the hand-curated YAML
comments and formatting in the schemas are never disturbed. If a
mapping is in the TSV but missing from the schema (or vice versa) the
script prints a diff and exits non-zero.

Subjects are resolved against schema *elements* (classes / slots /
enums / types) and against enum *permissible values* - the latter is
how the GAI risk categories carry their cross-framework mappings via
the ``GaiRiskCategoryEnum`` permissible values.

One category of SSSOM subject is intentionally *not* owned here and is
reported separately rather than as a failure:

* **Other-namespace subjects** (e.g. ``nist_ai_rmf:`` or
  ``nist_ai_100_1:``) live in sibling schemas; this repository only
  owns ``nist_ai_600_1`` elements.

Run via ``just verify-mappings`` (or directly:
``python scripts/verify_mappings.py``).
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
from collections import defaultdict
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_DIR = REPO_ROOT / "src" / "nist_ai_600_1" / "schema"
MAPPINGS_DIR = REPO_ROOT / "src" / "nist_ai_600_1" / "mappings"

# SSSOM subject prefix -> the schema YAML files that *define* those
# subjects. ``nist_ai_600_1`` owns a single schema file; the shared
# ``nist_ai_rmf_common`` base it imports is owned by ``nist_ai_100_1``
# and is therefore treated as an other-namespace subject below.
SUBJECT_TO_SCHEMAS: dict[str, list[Path]] = {
    "nist_ai_600_1": [
        SCHEMA_DIR / "nist_ai_600_1.yaml",
    ],
}

PREDICATE_TO_FIELD: dict[str, str] = {
    "skos:exactMatch": "exact_mappings",
    "skos:closeMatch": "close_mappings",
    "skos:broadMatch": "broad_mappings",
    "skos:narrowMatch": "narrow_mappings",
    "skos:relatedMatch": "related_mappings",
}

ELEMENT_SECTIONS = ("classes", "slots", "enums", "types")


def parse_sssom_tsv(path: Path) -> list[dict[str, str]]:
    """Return the SSSOM data rows (header comment lines are skipped)."""
    text_lines = [
        ln for ln in path.read_text().splitlines() if not ln.lstrip().startswith("#")
    ]
    reader = csv.DictReader(io.StringIO("\n".join(text_lines)), delimiter="\t")
    return [row for row in reader if row.get("subject_id")]


def load_schemas() -> dict[str, list[dict]]:
    """``{prefix: [parsed schema dict, ...]}`` for every owned prefix."""
    return {
        prefix: [yaml.safe_load(p.read_text()) for p in paths]
        for prefix, paths in SUBJECT_TO_SCHEMAS.items()
    }


def find_element(schemas: list[dict], name: str) -> tuple[dict, str] | None:
    """Locate ``name`` across the given schemas; return (element, section).

    A subject is matched against a top-level element (class / slot /
    enum / type), against an enum *permissible value* - the latter lets
    the GAI risk categories carry mappings on the ``GaiRiskCategoryEnum``
    permissible values - or against an inline class *attribute* (which
    LinkML treats as a locally-scoped slot, e.g. ``lifecycle_stage``).
    """
    for schema in schemas:
        for section in ELEMENT_SECTIONS:
            element = (schema.get(section) or {}).get(name)
            if element is not None:
                return element, section
    for schema in schemas:
        for enum_name, enum in (schema.get("enums") or {}).items():
            pv = (enum.get("permissible_values") or {}).get(name)
            if pv is not None:
                return pv, f"enums.{enum_name}.permissible_values"
    for schema in schemas:
        for class_name, cls in (schema.get("classes") or {}).items():
            attrs = (cls or {}).get("attributes") or {}
            if name in attrs:
                return attrs[name], f"classes.{class_name}.attributes"
    return None


def actual_mappings(element: dict) -> dict[str, set[str]]:
    """Read mapping fields off a schema element."""
    return {
        field: set(element.get(field) or []) for field in PREDICATE_TO_FIELD.values()
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Also fail when the schema has mappings that the TSV does not declare.",
    )
    args = parser.parse_args(argv)

    schemas_by_prefix = load_schemas()

    # Aggregate expected mappings across *all* TSV files before comparing,
    # so a mapping declared in one file is not flagged as missing/extra when
    # the same subject is mentioned in another file.
    # {prefix: {local_name: {field: {object_curie, ...}}}}
    expected: dict[str, dict[str, dict[str, set[str]]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(set))
    )
    other_namespace: set[str] = set()
    bad_predicate: list[str] = []

    for tsv in sorted(MAPPINGS_DIR.glob("*.sssom.tsv")):
        rows = parse_sssom_tsv(tsv)
        print(f"== {tsv.name} ({len(rows)} mappings) ==")
        for row in rows:
            subject = row["subject_id"]
            prefix, _, local = subject.partition(":")
            if prefix not in schemas_by_prefix:
                other_namespace.add(subject)
                continue
            predicate = row["predicate_id"]
            field = PREDICATE_TO_FIELD.get(predicate)
            if field is None:
                bad_predicate.append(f"{subject}: unsupported predicate {predicate!r}")
                continue
            expected[prefix][local][field].add(row["object_id"])

    overall_missing: list[str] = []
    overall_extra: list[str] = []
    overall_unknown: list[str] = []

    for prefix, elements in expected.items():
        schemas = schemas_by_prefix[prefix]
        for name, fields in sorted(elements.items()):
            found = find_element(schemas, name)
            if found is None:
                msg = f"{prefix}: element {name!r} not found in schema"
                overall_unknown.append(msg)
                print(f"  MISSING-ELEMENT: {msg}")
                continue
            element, section = found
            actual = actual_mappings(element)
            for field, exp_set in fields.items():
                act_set = actual.get(field, set())
                missing = exp_set - act_set
                extra = act_set - exp_set
                if missing:
                    msg = f"{prefix}: {section}.{name}.{field} missing: {sorted(missing)}"
                    overall_missing.append(msg)
                    print(f"  MISSING: {msg}")
                if extra and args.strict:
                    msg = (
                        f"{prefix}: {section}.{name}.{field} "
                        f"extra (not in TSV): {sorted(extra)}"
                    )
                    overall_extra.append(msg)
                    print(f"  EXTRA: {msg}")

    if other_namespace:
        print(
            f"  INFO: {len(other_namespace)} sibling-schema subject(s) "
            f"skipped (not owned here): {sorted(other_namespace)[:3]}..."
        )
    for msg in bad_predicate:
        print(f"  WARNING: {msg}", file=sys.stderr)

    if not (overall_missing or overall_unknown):
        print("  OK: schema mappings are in sync with the SSSOM TSV files")

    print()
    print(
        f"Summary: missing={len(overall_missing)} extra={len(overall_extra)} "
        f"unknown={len(overall_unknown)} "
        f"(skipped: {len(other_namespace)} sibling-schema subject(s))"
    )
    if overall_missing or overall_unknown:
        print(
            "\nApply the missing mappings to the schema YAML, "
            "or remove the rows from the SSSOM TSV.",
            file=sys.stderr,
        )
        return 1
    if overall_extra and args.strict:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
