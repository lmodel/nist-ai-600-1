# About nist-ai-600-1

NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0),
Generative Artificial Intelligence Profile (NIST AI 600-1, July 2024) -
LinkML Schema.

## Project status

Active development. The schema is **standalone** (it inlines the minimal
AI RMF 1.0 scaffolding it needs) and tracks the published NIST AI 600-1
document.

### Schema coverage

The single source schema
[src/nist_ai_600_1/schema/nist_ai_600_1.yaml](https://github.com/lmodel/nist-ai-600-1/blob/main/src/nist_ai_600_1/schema/nist_ai_600_1.yaml)
currently defines:

- **7 classes** - `NamedThingGAI`, `GaiRisk`, `SuggestedAction`,
  `PrimaryGaiConsideration`, `StructuredPublicFeedback`,
  `AiRedTeaming`, and the top-level `GaiProfile` container.
- **12 enums** covering AI lifecycle stages, trustworthiness
  characteristics, AI actor tasks, GAI risk categories /
  categorization / scope / sources / time scale, the
  GOVERN/MAP/MEASURE/MANAGE action function prefixes, primary
  considerations, structured-feedback methods, red-teaming types,
  provenance techniques, and governance practices.
- **2 types** - `GaiActionId` and `SubcategoryCode`.

### Cross-vocabulary mappings

Authoritative cross-references to NIST AI 100-1, NIST CSF v2, OSCAL,
ISO 27001 / 29100, gist, and STIX are tracked as SSSOM rows in
[src/nist_ai_600_1/mappings/nist_ai_600_1.sssom.tsv](https://github.com/lmodel/nist-ai-600-1/blob/main/src/nist_ai_600_1/mappings/nist_ai_600_1.sssom.tsv)
(21 mappings at present). The
[scripts/verify_mappings.py](https://github.com/lmodel/nist-ai-600-1/blob/main/scripts/verify_mappings.py)
checker keeps the TSV and the schema's `*_mappings` slots in sync; it
runs as part of `just test` (and is also available as
`just verify-mappings`).

### Test corpus

- **12 valid** fixtures under `tests/data/valid/` exercising each
  top-level class.
- **8 invalid** fixtures under `tests/data/invalid/` covering unknown
  slots and out-of-range enum values.
- Loader-level tests live in `tests/test_data.py`; structural /
  pattern rules are intended for a future `linkml-validate`-based
  suite.

### Generated artefacts

`just gen-project` produces the standard LinkML targets (Python
dataclasses + Pydantic, JSON Schema, JSON-LD context, OWL, SHACL,
ShEx, SQL DDL, GraphQL, Protobuf, Excel, TypeScript) under
[project/](https://github.com/lmodel/nist-ai-600-1/tree/main/project),
and `just gen-doc` produces the per-element Markdown under
[docs/elements/](elements/index.md) that backs this documentation
site.

## Roadmap

- Expand the SSSOM mapping set as sibling lmodel schemas
  (NIST AI 100-1, NIST CSF v2, OSCAL catalog / profile) stabilise.
- Add `linkml-validate`-based structural tests for cardinality and
  pattern rules.
- Grow the valid / invalid fixture corpus to cover every enum value
  and slot.

## References

- NIST AI 600-1: *Artificial Intelligence Risk Management Framework:
  Generative Artificial Intelligence Profile* (NIST AI 600-1, July 2024).
- NIST AI 100-1: *Artificial Intelligence Risk Management Framework
  (AI RMF 1.0)*.
