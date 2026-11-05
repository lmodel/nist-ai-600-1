---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/explanations/mappings
genre: explanation
title: Mappings
description: "What the schema crosses to: lmodel/nist-ai-100-1, lmodel/oscal, lmodel/stix and lmodel/spdx, each read at its source. The two SSSOM sets and their mappings to OWASP lists are gone, because a matching tool wrote their rows and no source confirmed them."
references:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/neighbour-copies
sources:
  - id: readme.md
    resource: README.md
    title: Mappings
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: test_mappings_name_a_class_of_the_neighbour
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Mappings

A risk has `related_mappings` to the AI RMF's risk. A suggested action has `broad_mappings` to OSCAL's part and `related_mappings` to STIX's course of action. The third-party control of asking for a software bill of materials has `related_mappings` to SPDX's `Sbom`.[^readme.md]

`tests/test_schema_rules.py` holds each to a copy in `tests/neighbours/`.[^test_schema_rules.py]

[^readme.md]: README.md, Mappings
[^test_schema_rules.py]: tests/test_schema_rules.py, test_mappings_name_a_class_of_the_neighbour
