---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/nist_ai_600_1/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/nist-ai-600-1-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project and gen-doc recipes
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
  - resource: .linkml/generators.yaml
  - resource: project
  - resource: src/nist_ai_600_1/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Generated artefacts

`just gen-project` writes the projections in `project/` and the Python models in `src/nist_ai_600_1/datamodel/`. `just gen-doc` writes the merged schema to `docs/schema/nist_ai_600_1.yaml` and the element pages to `docs/elements/`, which git ignores.[^justfile]

`project/jsonschema/nist_ai_600_1.schema.json` is what a consumer without LinkML validates with. `tests/test_catalogue.py` validates the whole catalogue with it, and loads the catalogue into the generated dataclasses and Pydantic models.[^test_catalogue.py]

[^justfile]: justfile, the gen-project and gen-doc recipes
[^test_catalogue.py]: tests/test_catalogue.py
