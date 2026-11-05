---
type: Reference
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/references/lmodel-nist-ai-100-1
genre: reference
title: lmodel/nist-ai-100-1
description: The lmodel repository that renders the AI RMF itself. This schema vendors its base and profiles modules, takes its AI actor tasks and trustworthiness characteristics, and holds its copy and its subcategories under `tests/`.
sources:
  - id: schema
    resource: src/nist_ai_600_1/schema/nist_ai_600_1.yaml
    title: the comments
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: VENDORED_PINS
source:
  - https://github.com/lmodel/nist-ai-100-1
generated:
  by: process:ktl-librarian
  at: "2026-11-05T03:00:36Z"
status: draft
---

# lmodel/nist-ai-100-1

This schema imports two of its modules, and `GaiProfile` is an `AiRmfProfile`.[^schema] Until that repository releases, the vendored files, its adapt copy and its list of subcategories come from its `feat/first-release` branch at commit `1ab8412`.[^test_upstream.py]

[^schema]: src/nist_ai_600_1/schema/nist_ai_600_1.yaml, the comments
[^test_upstream.py]: tests/test_upstream.py, VENDORED_PINS
