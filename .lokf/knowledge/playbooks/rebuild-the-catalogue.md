---
type: Playbook
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/playbooks/rebuild-the-catalogue
genre: how-to
title: Rebuild the catalogue
description: "How to refresh the tables in `src/nist_ai_600_1/data/ai-600-1.yaml`: run `just build-catalogue` after a change in `upstream/`, read the diff, and run `just test`. `just check-catalogue` compares without writing."
references:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/catalogue
sources:
  - id: builder
    resource: scripts/build_catalogue.py
    title: the docstring
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
    title: test_corrections_to_the_tables_are_the_listed_ones
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Rebuild the catalogue

1. Run `just build-catalogue`. It writes the tables and leaves section 2 and Appendix A as they are.[^builder]
2. Read the diff. A row the builder does not recognize stops it, and `tests/test_catalogue.py` lists each correction.[^test_catalogue.py]
3. Run `just test`.[^test_catalogue.py]

[^builder]: scripts/build_catalogue.py, the docstring
[^test_catalogue.py]: tests/test_catalogue.py, test_corrections_to_the_tables_are_the_listed_ones
