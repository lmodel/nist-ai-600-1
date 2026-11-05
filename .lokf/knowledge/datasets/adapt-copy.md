---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/nist-ai-600-1.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: five classes rooted on `Concept`, `ai_rmf_id` dropped for LOKF's `id`, `title` and `description` folded into LOKF's, and two designators demoted."
resource: .lokf/nist-ai-600-1.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/nist-ai-600-1-linkml-schema
about:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/glossary/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - resource: .lokf/nist-ai-600-1.yaml
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the schema setting
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# The schema's adapt copy

`just lokf-adapt` writes `.lokf/nist-ai-600-1.yaml` from the umbrella, and `just lokf-adapt-check` fails when it is stale. CI runs the check.[^project.justfile]

The README lists the concept types for the *Known LOKF types* setting. A release attaches the copy as `schema-<tag>-nist-ai-600-1.yaml`.[^readme.md]

[^project.justfile]: project.justfile, the comment above the recipes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
