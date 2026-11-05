---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/example-data
genre: reference
title: Example data
description: "The examples `tests/test_data.py` checks: a valid example of each class that is not abstract, and a counter-example for each constraint, whose first line names where it must fail."
resource: tests/data
references:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/nist-ai-600-1-linkml-schema
sources:
  - id: test_data.py
    resource: tests/test_data.py
  - resource: tests/data
  - resource: tests/__init__.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Example data

Each file under `tests/data/valid/` or `tests/data/invalid/` is named after the class it is checked against.[^test_data.py]

Each counter-example's first line, `# Fails at: <pointer>`, names where the validator must fail, so a file that starts failing for another reason fails the test.[^test_data.py]

[^test_data.py]: tests/test_data.py
