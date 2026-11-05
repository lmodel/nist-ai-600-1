---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/nist-ai-600-1-linkml-schema
genre: reference
title: nist-ai-600-1 LinkML schema
description: "The LinkML model of NIST AI 600-1, `src/nist_ai_600_1/schema/nist_ai_600_1.yaml`: an umbrella over three modules and the vendored AI RMF slice that holds the tree root `GaiProfile`, with the `Gai` class prefix and the `gai_` slot prefix."
resource: src/nist_ai_600_1/schema/nist_ai_600_1.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/references/nist-ai-600-1
hasPart:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/risks-module
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/actions-module
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/considerations-module
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/vendored-modules
sources:
  - id: schema
    resource: src/nist_ai_600_1/schema/nist_ai_600_1.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# nist-ai-600-1 LinkML schema

The umbrella imports `nist_ai_600_1_risks`, `nist_ai_600_1_actions`, `nist_ai_600_1_considerations` and the vendored modules, and declares `GaiProfile`.[^schema]

The publication has no version of its own, so `version` is the 1.0.0 of the AI RMF it profiles, and `source` is the publication's digital object identifier.[^schema]

[^schema]: src/nist_ai_600_1/schema/nist_ai_600_1.yaml
