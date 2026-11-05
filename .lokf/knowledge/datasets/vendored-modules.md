---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/vendored-modules
genre: reference
title: Vendored AI RMF modules
description: "`src/nist_ai_600_1/schema/nist_ai_100_1/`: the base and profiles modules of lmodel/nist-ai-100-1, unchanged and pinned by SHA-256 in `tests/test_upstream.py`, so the schema needs no network."
resource: src/nist_ai_600_1/schema/nist_ai_100_1
isPartOf:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/nist-ai-600-1-linkml-schema
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/references/lmodel-nist-ai-100-1
sources:
  - id: base
    resource: src/nist_ai_600_1/schema/nist_ai_100_1/nist_ai_100_1_base.yaml
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: VENDORED_PINS
  - resource: src/nist_ai_600_1/schema/nist_ai_100_1/nist_ai_100_1_profiles.yaml
  - resource: tests/ai_rmf_subcategories.yaml
    title: the subcategories as lmodel/nist-ai-100-1 states them
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Vendored AI RMF modules

They give the identifier form of a subcategory, the trustworthiness characteristics, the AI actor tasks with the tables' spellings as aliases, `AiRmfRecord` and `AiRmfProfile`.[^base]

`tests/test_upstream.py` holds them to their hashes, and says to vendor from the release and move the pins once that repository releases.[^test_upstream.py]

[^base]: src/nist_ai_600_1/schema/nist_ai_100_1/nist_ai_100_1_base.yaml
[^test_upstream.py]: tests/test_upstream.py, VENDORED_PINS
