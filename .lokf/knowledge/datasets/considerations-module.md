---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/considerations-module
genre: reference
title: Considerations module
description: "`nist_ai_600_1_considerations.yaml`: a class for each of Appendix A's four primary considerations, the kinds of structured public feedback, and the lists of governance plans, third-party controls, provenance techniques and incident harms."
resource: src/nist_ai_600_1/schema/nist_ai_600_1_considerations.yaml
isPartOf:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/nist-ai-600-1-linkml-schema
sources:
  - id: considerations
    resource: src/nist_ai_600_1/schema/nist_ai_600_1_considerations.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Considerations module

`GaiPrimaryConsideration` is abstract, and `gai_consideration_type` names which of its four classes a record is.[^considerations]

`GaiStructuredFeedback` works the same way for participatory engagement, field testing and AI red-teaming, under Pre-Deployment Testing.[^considerations]

[^considerations]: src/nist_ai_600_1/schema/nist_ai_600_1_considerations.yaml
