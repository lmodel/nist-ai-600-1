---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: The adapt copies of 19 released lmodel repositories in `tests/neighbours/`, among them oscal, stix and spdx, each pinned by its SHA-256, and lmodel/nist-ai-100-1's copy from its branch. `tests/test_schema_rules.py` holds this schema's copy apart from them and checks the mappings.
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
  - resource: tests/neighbours
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Neighbours' adapt copies

Each file is the schema asset of a lmodel release, pinned in `tests/test_schema_rules.py` by its checksum.[^test_schema_rules.py]

The test fails on a shared class, enum, type or subset, and on a shared key it does not list.[^test_schema_rules.py]

`nist-ai-100-1.yaml` comes from that repository's `feat/first-release` branch until it releases. This copy shares the vendored names with it, each spelled alike.[^test_schema_rules.py]

[^test_schema_rules.py]: tests/test_schema_rules.py
