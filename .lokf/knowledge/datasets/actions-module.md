---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/actions-module
genre: reference
title: Actions module
description: "`nist_ai_600_1_actions.yaml`: `GaiSubcategory`, one table of section 3, and `GaiSuggestedAction`, one row with its Action ID, text and risk tags. AI actor tasks belong to the table."
resource: src/nist_ai_600_1/schema/nist_ai_600_1_actions.yaml
isPartOf:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/nist-ai-600-1-linkml-schema
sources:
  - id: actions
    resource: src/nist_ai_600_1/schema/nist_ai_600_1_actions.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Actions module

A table names an AI RMF subcategory, restates it, lists at least one action and names its AI actor tasks.[^actions]

An Action ID such as `GV-1.1-001` gives the function's two letters, the subcategory's numbers and a three-digit number.[^actions]

[^actions]: src/nist_ai_600_1/schema/nist_ai_600_1_actions.yaml
