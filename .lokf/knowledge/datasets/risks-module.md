---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/risks-module
genre: reference
title: Risks module
description: "`nist_ai_600_1_risks.yaml`: `GaiRisk`, the enum of 12 risks with the tables' spellings as aliases, the groupings of footnote 5, and the lifecycle, scope, source and time-scale values of section 2."
resource: src/nist_ai_600_1/schema/nist_ai_600_1_risks.yaml
isPartOf:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/nist-ai-600-1-linkml-schema
sources:
  - id: risks
    resource: src/nist_ai_600_1/schema/nist_ai_600_1_risks.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Risks module

`GaiRisk` carries a section, a definition, trustworthiness characteristics and groupings from the publication.[^risks]

It also carries lifecycle stages, scopes, sources and time scales, which the publication assigns to no risk, for an adopter to fill.[^risks]

[^risks]: src/nist_ai_600_1/schema/nist_ai_600_1_risks.yaml
