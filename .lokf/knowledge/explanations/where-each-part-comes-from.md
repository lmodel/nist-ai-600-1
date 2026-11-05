---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/explanations/where-each-part-comes-from
genre: explanation
title: Where each part comes from
description: NIST publishes no machine-readable form of the Profile, so a script reads the tables of section 3 from the PDF, and tests hold section 2's definitions and Appendix A's lists to its words. The AI RMF's own terms come from lmodel/nist-ai-100-1.
references:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/catalogue
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/vendored-modules
sources:
  - id: about
    resource: docs/about.md
    title: Where each part comes from
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Where each part comes from

The publication is the only source, and `upstream/` holds it unchanged.[^about]

The schema's descriptions are this project's own words. The catalogue's definitions, statements and actions are NIST's.[^about]

The base and profiles modules of lmodel/nist-ai-100-1 give a subcategory's identifier form, the trustworthiness characteristics, the AI actor tasks and the profile.[^about]

[^about]: docs/about.md, Where each part comes from
