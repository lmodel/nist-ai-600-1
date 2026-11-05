---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/upstream-copy
genre: reference
title: Copy of the upstream
description: "`upstream/NIST.AI.600-1.pdf`: the publication, unchanged, which `scripts/check_upstream_release.py` pins by SHA-256 and `tests/test_upstream.py` compares offline."
resource: upstream
about:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/references/nist-ai-600-1
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
  - resource: upstream
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Copy of the upstream

The PDF is pinned by SHA-256, as of 2026-11-05.[^watch]

`tests/test_upstream.py` fails on a file that differs or a file nobody pinned.[^test_upstream.py]

[^watch]: scripts/check_upstream_release.py, the pins
[^test_upstream.py]: tests/test_upstream.py
