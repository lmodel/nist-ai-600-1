---
type: Playbook
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Move to another edition
description: "How to move the schema when the watch reports a change, or to the release of lmodel/nist-ai-100-1: read what changed, then move `upstream/`, the pins and the headers together, or the vendored modules and their pins, and run the tests."
references:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/workflows/upstream-watch
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/upstream-copy
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: VENDORED_PINS
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Move to another edition

1. Read the watch's report and what NIST changed. A person decides whether the schema moves.[^watch]
2. Replace the file in `upstream/`, and move its pin in `scripts/check_upstream_release.py`.[^watch]
3. Run `just build-catalogue` and `just test`.[^contributing.md]

When lmodel/nist-ai-100-1 releases, vendor its modules and its asset, and move `VENDORED_PINS` and the neighbour's checksum.[^test_upstream.py]

[^watch]: scripts/check_upstream_release.py, the pins
[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^test_upstream.py]: tests/test_upstream.py, VENDORED_PINS
