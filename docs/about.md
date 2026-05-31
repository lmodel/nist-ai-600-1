# About nist-ai-600-1

NIST Artificial Intelligence Risk Management Framework (AI RMF 1.0), Generative Artificial Intelligence Profile (NIST AI 600-1, July 2024) - LinkML Schema.

## Project status

Active development, tracking the published NIST AI 600-1 document.

### Design

The schema imports the shared **`nist_ai_rmf_common`** module (hosted in [`nist-ai-100-1`](https://github.com/lmodel/nist-ai-100-1)) for the framework base — the `NamedThing` root, identifier/title/description slots, `SubcategoryCode`, and `TrustworthinessCharacteristicEnum` — so those have one canonical definition shared with NIST AI 100-1 and the
`nist-ai-rmf` umbrella. The GAI lifecycle and actor-task vocabularies genuinely diverge from AI RMF 1.0, so they are defined locally as `GaiLifecycleStageEnum` / `GaiActorTaskEnum` and attached as **class-local attributes** (`lifecycle_stage` on `GaiRisk`, `actor_task` on `SuggestedAction`) — keeping them out of the merged global slot namespace so they never collide with the 100-1 enums in the umbrella.

### Schema coverage

The single source schema [src/nist_ai_600_1/schema/nist_ai_600_1.yaml](https://github.com/lmodel/nist-ai-600-1/blob/main/src/nist_ai_600_1/schema/nist_ai_600_1.yaml) currently defines:

- **6 classes** - `GaiRisk`, `SuggestedAction`,
  `PrimaryGaiConsideration`, `StructuredPublicFeedback`,
  `AiRedTeaming`, and the top-level `GaiProfile` container (all derive
  from the imported `NamedThing`).
- **13 enums** covering GAI lifecycle stages (`GaiLifecycleStageEnum`)
  and actor tasks (`GaiActorTaskEnum`), GAI risk categories /
  categorization / scope / sources / time scale, the
  GOVERN/MAP/MEASURE/MANAGE action function prefixes, primary
  considerations, structured-feedback methods, red-teaming types,
  provenance techniques, and governance practices. The shared
  `TrustworthinessCharacteristicEnum` is imported from common.
- **1 type** - `GaiActionId` (`SubcategoryCode` is imported from common).

### Cross-vocabulary mappings

Two SSSOM TSVs live under `src/nist_ai_600_1/mappings/`:

- **[`nist_ai_600_1.sssom.tsv`](https://github.com/lmodel/nist-ai-600-1/blob/main/src/nist_ai_600_1/mappings/nist_ai_600_1.sssom.tsv)** (17 mappings) — the schema's own cross-references to NIST AI 100-1, NIST CSF v2, OSCAL, ISO 27001 / 29100, gist, and STIX.
- **[`nist_ai_rmf.sssom.tsv`](https://github.com/lmodel/nist-ai-600-1/blob/main/src/nist_ai_600_1/mappings/nist_ai_rmf.sssom.tsv)** — the cross-framework alignment set shared with the `nist-ai-rmf` umbrella. Its `nist_ai_600_1`-owned rows bind the OWASP Agentic AI (ASI) Top 10 onto the `GaiRiskCategoryEnum` permissible values; rows whose subject belongs to a sibling schema (`nist_ai_100_1` / `nist_ai_rmf`) are reported and skipped.

The [scripts/verify_mappings.py](https://github.com/lmodel/nist-ai-600-1/blob/main/scripts/verify_mappings.py)
checker keeps every TSV row in sync with the matching schema element — top-level classes / slots / enums / types, enum permissible values, and class-local attributes — and reports `missing=0 extra=0 unknown=0` (20 sibling-schema subjects skipped). It runs as part of `just test` (and is also available as
`just verify-mappings`).

### Test corpus

- **12 valid** fixtures under `tests/data/valid/` exercising each top-level class.
- **8 invalid** fixtures under `tests/data/invalid/` covering unknown slots and out-of-range enum values.
- Loader-level tests live in `tests/test_data.py`; structural /
 attern rules are intended for a future `linkml-validate`-based suite.

### Generated artefacts

`just gen-project` produces the standard LinkML targets (Python dataclasses + Pydantic, JSON Schema, JSON-LD context, OWL, SHACL, ShEx, SQL DDL, GraphQL, Protobuf, Excel, TypeScript) under [project/](https://github.com/lmodel/nist-ai-600-1/tree/main/project), and `just gen-doc` produces the per-element Markdown under [docs/elements/](elements/index.md) that backs this documentation
site.

## Roadmap

- Expand the SSSOM mapping set as sibling lmodel schemas (NIST AI 100-1, NIST CSF v2, OSCAL catalog / profile) stabilise.
- Add `linkml-validate`-based structural tests for cardinality and pattern rules.
- Grow the valid / invalid fixture corpus to cover every enum value and slot.

## References

- NIST AI 600-1: *Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile* (NIST AI 600-1, July 2024).
- NIST AI 100-1: *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*.
