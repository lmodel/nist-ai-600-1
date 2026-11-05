---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/catalogue
genre: reference
title: The catalogue
description: "`src/nist_ai_600_1/data/ai-600-1.yaml`, the whole Profile as one `GaiProfile` record: 12 risks, 49 tables, 212 suggested actions and four primary considerations."
resource: src/nist_ai_600_1/data/ai-600-1.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/references/nist-ai-600-1
sources:
  - id: builder
    resource: scripts/build_catalogue.py
    title: the docstring
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
  - resource: project.justfile
    title: the catalogue recipes
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# The catalogue

`scripts/build_catalogue.py` writes the tables of section 3 from the PDF, and section 2 and Appendix A are written by hand.[^builder]

`tests/test_catalogue.py` validates the file with `linkml-validate` and the committed JSON Schema, loads it into both generated models, and holds it to the publication's words, counts and numbering.[^test_catalogue.py]

Actions by function: Govern 58, Map 39, Measure 72, Manage 43.[^test_catalogue.py]

[^builder]: scripts/build_catalogue.py, the docstring
[^test_catalogue.py]: tests/test_catalogue.py
