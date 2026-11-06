# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `nist-ai-600-1.yaml`, as KTL v0.62.0 lays them out.

## [0.1.0] - 2026-11-05

### Added

- **The whole Profile as records** in `src/nist_ai_600_1/data/ai-600-1.yaml`: the 12 risks with their definitions and characteristics, the 49 tables with their 212 suggested actions, and the four primary considerations. `scripts/build_catalogue.py` writes the tables from the publication.
- **`upstream/`**, holding the publication, with a weekly watch that reports a change to it. The watch reads only https addresses on NIST's host, at the start and after a redirect.
- **Section numbers on risks, and classes for each primary consideration**, with the third-party controls of section A.1.3 and the kinds of harm in section A.1.8's definition of an AI incident.
- **Tests** that validate the whole catalogue, hold it to the publication's words, counts and numbering, and list each correction the builder makes. An example per class and a counter-example per constraint, each naming where it fails.
- **`.lokf/nist-ai-600-1.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-nist-ai-600-1.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, NOTICE and the CONTRIBUTING checklist.

### Changed

- **The schema splits into modules**: `nist_ai_600_1_risks`, `nist_ai_600_1_actions`, `nist_ai_600_1_considerations` and the umbrella. Classes and enums take the `Gai` prefix, slots the `gai_` prefix and values snake_case.
- **It vendors the base and profiles modules of lmodel/nist-ai-100-1** in place of an import by address, so it needs no network and cannot move under a release. `GaiProfile` is now an `AiRmfProfile`.
- **AI actor tasks move from an action to its table**, as the publication has them, and take lmodel/nist-ai-100-1's enum.
- **A risk's groupings become a list**, since footnote 5 lists Data Privacy under all three.
- **Each primary consideration is a class of its own**, in place of one class with a kind and fields that apply only to some kinds. Structured feedback does the same.
- **Mappings name classes the released neighbours hold**, and tests check each. A table and an action take `related_mappings` to the AI RMF's subcategory and suggested action.
- **The template settings** turn PyPI publishing and the docs preview off, linkml and linkml-runtime are locked at 1.12.1, and the Python project is named `nist-ai-600-1-linkml`.

### Removed

- **`function_prefix`, the action's own `id` and `addressed_by_actions`**, each of which restated another field.
- **`GaiActorTaskEnum`**, in favour of lmodel/nist-ai-100-1's enum, whose aliases hold the spellings the tables use.
- **The two SSSOM sets, their verifier and their test**, whose rows came from a matching tool and no source confirmed. The mappings to OWASP lists went with them. The umbrella set stays in lmodel/nist-ai-rmf.
- **The mkdocs site**, with redirects from its addresses to the new site.
