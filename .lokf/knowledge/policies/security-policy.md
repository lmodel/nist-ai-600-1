---
type: Policy
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in NIST's own text belongs with NIST.
resource: SECURITY.md
references:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/workflows/upstream-watch
sources:
  - id: security.md
    resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Security policy

Report a vulnerability through GitHub's private vulnerability reporting. Only the latest release receives fixes.[^security.md]

The release carries the adapt copy, the bundle as a zip and a Copilot skill zip, each with a checksum and a build-provenance attestation.[^security.md]

The catalogue's text is NIST's, and this repository treats it as data. Tests validate it, and nothing executes or renders it.[^security.md]

`scripts/check_upstream_release.py` runs only in the weekly watch. It follows a redirect only over https.[^security.md]

[^security.md]: SECURITY.md
