---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/explanations/faults-in-the-publication
genre: explanation
title: Faults in the publication
description: "What the catalogue corrects in the tables, each listed in the builder and held by a test: the identifier GV4.3--001, the tag Civil Rights violations on GV-1.4-002, and one row with a missing semicolon. Two further faults stay as they are."
about:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/references/nist-ai-600-1
sources:
  - id: builder
    resource: scripts/build_catalogue.py
    title: ID_TYPOS, NOT_A_RISK and JOINED_TAGS
  - id: about
    resource: docs/about.md
    title: What the publication gets wrong, and what the catalogue does
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Faults in the publication

The builder writes `GV-4.3-001` for `GV4.3--001`, leaves out the tag Civil Rights violations, which is not one of the 12 risks, and splits a row that runs two tags together.[^builder]

The restatement of GOVERN 1.5 differs from AI 100-1's Table 1, and the catalogue keeps this publication's wording.[^about]

Section 2 says tables in Appendix B map risks to trustworthiness characteristics. Appendix B holds the references, and the subsections of section 2 name the characteristics, so the catalogue takes them from there.[^about]

[^builder]: scripts/build_catalogue.py, ID_TYPOS, NOT_A_RISK and JOINED_TAGS
[^about]: docs/about.md, What the publication gets wrong, and what the catalogue does
