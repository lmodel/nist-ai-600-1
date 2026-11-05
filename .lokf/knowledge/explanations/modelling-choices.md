---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/explanations/modelling-choices
genre: explanation
title: Modelling choices
description: Why AI actor tasks belong to a table and not an action, why a risk's groupings are a list, why Pre-Deployment Testing holds structured feedback, and why each primary consideration is a class of its own.
about:
  - https://w3id.org/lmodel/nist-ai-600-1/knowledge/datasets/nist-ai-600-1-linkml-schema
sources:
  - id: about
    resource: docs/about.md
    title: Choices worth knowing
  - id: changelog
    resource: CHANGELOG.md
    title: Changed
generated:
  by: process:ktl-librarian
  at: "2026-11-05T02:56:42Z"
status: draft
---

# Modelling choices

The publication says not every task listed applies to every action, so tasks sit on the table.[^about]

Footnote 5 offers the groupings as one possible way to sort the risks, and lists Data Privacy under all three.[^about]

Section A.1.7 calls the feedback approaches part of Pre-Deployment Testing, although section A.1.5 has a heading of its own.[^about]

Each consideration has lists of its own, so a class for each replaces one class with fields that apply to some kinds only.[^changelog]

[^about]: docs/about.md, Choices worth knowing
[^changelog]: CHANGELOG.md, Changed
