---
type: Service
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: other bytes at NIST's address for the publication fail the run and open or update an issue."
resource: .github/workflows/upstream-watch.yaml
about:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/references/nist-ai-600-1
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the docstring
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the docstring
  - resource: .github/scripts/report-issue.sh
    title: how the issue is opened
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday, and a failing check opens an issue or comments on the one already open.[^upstream-watch.yaml]

The script downloads the publication with no token, following a redirect only over https, and compares its SHA-256.[^watch]

`tests/test_watch.py` runs it against stubbed downloads.[^test_watch.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^watch]: scripts/check_upstream_release.py, the docstring
[^test_watch.py]: tests/test_watch.py, the docstring
