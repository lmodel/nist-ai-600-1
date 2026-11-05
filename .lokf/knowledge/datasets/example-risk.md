---
type: GaiRisk
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/example-risk
genre: reference
title: Confabulation
description: The risk of confabulation, written as a concept of type `GaiRisk` in the adapt copy's keys. It shows that the domain schema admits a risk as a concept, with the keys an adopter fills in.
resource: tests/data/valid/GaiRisk-an-adopters-assessment.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/catalogue
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: example
    resource: tests/data/valid/GaiRisk-an-adopters-assessment.yaml
gai_risk_name: confabulation
gai_risk_section: "2.2"
gai_risk_lifecycle_stages:
  - operation
gai_risk_scopes:
  - application_or_implementation
gai_risk_sources:
  - outputs
gai_risk_time_scales:
  - abrupt
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Confabulation

A concept may name a class the README lists as its `type`, with the copy's keys beside LOKF's.[^readme.md] This one comes from a valid example.[^example]

[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^example]: tests/data/valid/GaiRisk-an-adopters-assessment.yaml
