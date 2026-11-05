#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pdfplumber>=0.11.7", "pyyaml>=6"]
# ///
"""Write section 3 of NIST AI 600-1 into src/nist_ai_600_1/data/ai-600-1.yaml.

Each table of section 3 begins with an AI RMF subcategory, lists suggested actions with
their risk tags, and ends with the AI Actor Tasks. This script reads those tables from
upstream/NIST.AI.600-1.pdf and corrects only what KNOWN_DEPARTURES lists. The rest of
the catalogue file is written by hand and stays as it is. With --check the script writes
nothing and exits 1 when the file differs from what the publication gives.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import pdfplumber
import yaml

ROOT = Path(__file__).resolve().parent.parent
PDF = ROOT / "upstream" / "NIST.AI.600-1.pdf"
CATALOGUE = ROOT / "src" / "nist_ai_600_1" / "data" / "ai-600-1.yaml"
SCHEMA_DIR = ROOT / "src" / "nist_ai_600_1" / "schema"

SUBCATEGORY = re.compile(r"((?:GOVERN|MAP|MEASURE|MANAGE) \d+\.\d+):\s*(.*)", re.S)
ACTION_ID = re.compile(r"(?:GV|MP|MS|MG)-\d+\.\d+-\d{3}")
LIGATURES = str.maketrans({"ﬀ": "ff", "ﬁ": "fi", "ﬂ": "fl", "ﬃ": "ffi", "ﬄ": "ffl"})

# What the tables print that a reader must correct, each with what it should say.
ID_TYPOS = {"GV4.3--001": "GV-4.3-001"}
# A tag that is none of the 12 risks, on the action that carries it. It is left out.
NOT_A_RISK = {("GV-1.4-002", "Civil Rights violations")}
# Tags the tables run together without their semicolon.
JOINED_TAGS = {
    "Human-AI Configuration, Dangerous, Violent, or Hateful Content": [
        "Human-AI Configuration",
        "Dangerous, Violent, or Hateful Content",
    ],
}


def text_of(cell: str) -> str:
    """A table cell as one line, with its line breaks and ligatures undone."""
    cell = cell.translate(LIGATURES)
    cell = re.sub(r"-\n", "-", cell)
    return re.sub(r"\s+", " ", cell).strip()


def table_rows(path: Path = PDF) -> list[list[str]]:
    """The non-empty cells of every table row in section 3, in order."""
    rows = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            if re.search(r"^Appendix A\. Primary GAI Considerations\s*$", text, re.M):
                break
            for table in page.extract_tables():
                for row in table:
                    cells = [cell for cell in row if cell and cell.strip()]
                    if cells:
                        rows.append(cells)
    return rows


def enum_names(module: Path, enum: str) -> dict[str, str]:
    """Each spelling of an enum's values, with the permissible value it names."""
    values = yaml.safe_load(module.read_text(encoding="utf-8"))["enums"][enum][
        "permissible_values"
    ]
    names = {}
    for value, entry in values.items():
        names[entry["title"]] = value
        for alias in entry.get("aliases", []):
            names[alias] = value
    return names


def split_tags(cell: str, action_id: str, names: dict[str, str]) -> list[str]:
    """The risk tags of one row, as permissible values, in the row's order."""
    tags: list[str] = []
    for tag in text_of(cell).split(";"):
        tag = tag.strip()
        if not tag or (action_id, tag) in NOT_A_RISK:
            continue
        tags.extend(JOINED_TAGS.get(tag, [tag]))
    return [names[tag] for tag in tags]


def section_three() -> list[dict]:
    """Each table of section 3 as one subcategory record."""
    risks = enum_names(SCHEMA_DIR / "nist_ai_600_1_risks.yaml", "GaiRiskName")
    tasks = enum_names(
        SCHEMA_DIR / "nist_ai_100_1" / "nist_ai_100_1_base.yaml", "AiRmfActorTaskName"
    )
    records: list[dict] = []
    current: dict | None = None
    in_head = False
    for cells in table_rows():
        first = text_of(cells[0])
        head = SUBCATEGORY.match(first)
        if head:
            current = {
                "ai_rmf_subcategory_id": head.group(1),
                "description": head.group(2),
                "gai_subcategory_actions": [],
            }
            records.append(current)
            in_head = True
        elif first == "Action ID":
            in_head = False
        elif in_head:
            current["description"] += " " + first
        elif ACTION_ID.fullmatch(first) or first in ID_TYPOS:
            action_id = ID_TYPOS.get(first, first)
            action = {"gai_action_id": action_id, "description": text_of(cells[1])}
            tags = split_tags(cells[2], action_id, risks) if len(cells) > 2 else []
            if tags:
                action["gai_action_risks"] = tags
            current["gai_subcategory_actions"].append(action)
        elif first.startswith(("AI Actor Tasks:", "AI Actors:")):
            names = first.split(":", 1)[1].split(",")
            current["gai_subcategory_actor_tasks"] = [
                tasks[name.strip()] for name in names
            ]
        else:
            raise ValueError(f"a row the tables should not hold: {cells}")
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="compare, and write nothing"
    )
    args = parser.parse_args()
    document = yaml.safe_load(CATALOGUE.read_text(encoding="utf-8"))
    built = section_three()
    if args.check:
        if document["gai_subcategories"] != built:
            print(
                f"{CATALOGUE} differs from what the publication gives", file=sys.stderr
            )
            return 1
        return 0
    document["gai_subcategories"] = built
    document["ai_rmf_profile_subcategories"] = [
        record["ai_rmf_subcategory_id"] for record in built
    ]
    CATALOGUE.write_text(
        yaml.safe_dump(document, sort_keys=False, allow_unicode=True, width=100),
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
