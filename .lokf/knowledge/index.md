---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/nist-ai-600-1/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: nist-ai-600-1 Knowledge Bundle
description: NIST AI 600-1 AI RMF Generative AI Profile (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/nist-ai-600-1/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# nist-ai-600-1 Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for nist-ai-600-1. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/nist-ai-600-1`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.

# Workflows

* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It starts by hand or, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, on each published release.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request that a person merges.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, and lints the schema and checks the adapt copy on 3.13.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: other bytes at NIST's address for the publication fail the run and open or update an issue.

# Playbooks

* [Release](playbooks/release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the schema: edit `src/nist_ai_600_1/schema/`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated files are never edited by hand.
* [Rebuild the catalogue](playbooks/rebuild-the-catalogue.md) - How to refresh the tables in `src/nist_ai_600_1/data/ai-600-1.yaml`: run `just build-catalogue` after a change in `upstream/`, read the diff, and run `just test`. `just check-catalogue` compares without writing.
* [Move to another edition](playbooks/update-upstream-pins.md) - How to move the schema when the watch reports a change, or to the release of lmodel/nist-ai-100-1: read what changed, then move `upstream/`, the pins and the headers together, or the vendored modules and their pins, and run the tests.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Glossary

* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.
* [Generative AI (GAI)](glossary/generative-ai.md) - The class of AI models that emulate the structure and characteristics of input data to generate derived synthetic content. The publication says GAI generally refers to generative foundation models.
* [GAI risk](glossary/gai-risk.md) - One of the 12 risks that section 2 defines as unique to or made worse by the development and use of GAI, such as Confabulation or Information Integrity.
* [Suggested action](glossary/suggested-action.md) - A step an organization or AI actor can take to manage GAI risks, named by an Action ID such as GV-1.1-001. Section 3 lists 212.
* [Primary consideration](glossary/primary-consideration.md) - One of four themes from NIST's Generative AI Public Working Group: Governance, Pre-Deployment Testing, Content Provenance and Incident Disclosure.
* [AI red-teaming](glossary/ai-red-teaming.md) - A structured testing exercise that probes an AI system for flaws and vulnerabilities, often in a controlled environment and with its developers. Section A.1.5 names four types.
* [Provenance data tracking](glossary/provenance-data-tracking.md) - Recording the origin and history of digital content, through metadata and digital watermarks, so its authenticity can be determined. Section A.1.6 names four techniques.
* [AI incident](glossary/ai-incident.md) - An event where developing, using or a malfunction of AI systems contributes to one of four kinds of harm, by the definition section A.1.8 quotes. An incident can be aggregate or acute.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: whoever submits owns the contribution, an element says what the publication says, a rule states only what the publication states, a mapping is read at its source, and no commit carries an AI co-authorship trailer.
* [Security policy](policies/security-policy.md) - How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in NIST's own text belongs with NIST.
* [Licence and attribution](policies/license-and-attribution.md) - Whose work each part is: the code and the schema under Apache-2.0, the bundle under CC BY 4.0, and the publication under NIST's statement, which allows reprints worldwide with its citation. No endorsement by NIST is implied.

# Datasets

* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/nist_ai_600_1/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - The adapt copies of 19 released lmodel repositories in `tests/neighbours/`, among them oscal, stix and spdx, each pinned by its SHA-256, and lmodel/nist-ai-100-1's copy from its branch. `tests/test_schema_rules.py` holds this schema's copy apart from them and checks the mappings.
* [Example data](datasets/example-data.md) - The examples `tests/test_data.py` checks: a valid example of each class that is not abstract, and a counter-example for each constraint, whose first line names where it must fail.
* [nist-ai-600-1 LinkML schema](datasets/nist-ai-600-1-linkml-schema.md) - The LinkML model of NIST AI 600-1, `src/nist_ai_600_1/schema/nist_ai_600_1.yaml`: an umbrella over three modules and the vendored AI RMF slice that holds the tree root `GaiProfile`, with the `Gai` class prefix and the `gai_` slot prefix.
* [Risks module](datasets/risks-module.md) - `nist_ai_600_1_risks.yaml`: `GaiRisk`, the enum of 12 risks with the tables' spellings as aliases, the groupings of footnote 5, and the lifecycle, scope, source and time-scale values of section 2.
* [Actions module](datasets/actions-module.md) - `nist_ai_600_1_actions.yaml`: `GaiSubcategory`, one table of section 3, and `GaiSuggestedAction`, one row with its Action ID, text and risk tags. AI actor tasks belong to the table.
* [Considerations module](datasets/considerations-module.md) - `nist_ai_600_1_considerations.yaml`: a class for each of Appendix A's four primary considerations, the kinds of structured public feedback, and the lists of governance plans, third-party controls, provenance techniques and incident harms.
* [Vendored AI RMF modules](datasets/vendored-modules.md) - `src/nist_ai_600_1/schema/nist_ai_100_1/`: the base and profiles modules of lmodel/nist-ai-100-1, unchanged and pinned by SHA-256 in `tests/test_upstream.py`, so the schema needs no network.
* [The catalogue](datasets/catalogue.md) - `src/nist_ai_600_1/data/ai-600-1.yaml`, the whole Profile as one `GaiProfile` record: 12 risks, 49 tables, 212 suggested actions and four primary considerations.
* [Copy of the upstream](datasets/upstream-copy.md) - `upstream/NIST.AI.600-1.pdf`: the publication, unchanged, which `scripts/check_upstream_release.py` pins by SHA-256 and `tests/test_upstream.py` compares offline.
* [The schema's adapt copy](datasets/adapt-copy.md) - `.lokf/schema/nist-ai-600-1.yaml`, the copy `just lokf-adapt` writes from the schema so that it sits beside LOKF's `lokf.yaml`: five classes rooted on `Concept`, `ai_rmf_id` dropped for LOKF's `id`, `title` and `description` folded into LOKF's, and two designators demoted.
* [Confabulation](datasets/example-risk.md) - The risk of confabulation, written as a concept of type `GaiRisk` in the adapt copy's keys. It shows that the domain schema admits a risk as a concept, with the keys an adopter fills in.

# References

* [NIST AI 600-1, the Generative AI Profile](references/nist-ai-600-1.md) - The publication this schema renders: Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile, NIST AI 600-1, July 2024. `upstream/NIST.AI.600-1.pdf` holds it, and NIST publishes no machine-readable form.
* [lmodel/nist-ai-100-1](references/lmodel-nist-ai-100-1.md) - The lmodel repository that renders the AI RMF itself. This schema vendors its base and profiles modules, takes its AI actor tasks and trustworthiness characteristics, and holds its copy and its subcategories under `tests/`.

# Explanations

* [Where each part comes from](explanations/where-each-part-comes-from.md) - NIST publishes no machine-readable form of the Profile, so a script reads the tables of section 3 from the PDF, and tests hold section 2's definitions and Appendix A's lists to its words. The AI RMF's own terms come from lmodel/nist-ai-100-1.
* [Faults in the publication](explanations/faults-in-the-publication.md) - What the catalogue corrects in the tables, each listed in the builder and held by a test: the identifier GV4.3--001, the tag Civil Rights violations on GV-1.4-002, and one row with a missing semicolon. Two further faults stay as they are.
* [Modelling choices](explanations/modelling-choices.md) - Why AI actor tasks belong to a table and not an action, why a risk's groupings are a list, why Pre-Deployment Testing holds structured feedback, and why each primary consideration is a class of its own.
* [Scope](explanations/scope.md) - What the schema leaves out: the discussion of each risk, the running prose of Appendix A, definitions quoted from third parties and the references of Appendix B. The AI RMF itself is lmodel/nist-ai-100-1.
* [Mappings](explanations/mappings.md) - What the schema crosses to: lmodel/nist-ai-100-1, lmodel/oscal, lmodel/stix and lmodel/spdx, each read at its source. The two SSSOM sets and their mappings to OWASP lists are gone, because a matching tool wrote their rows and no source confirmed them.
