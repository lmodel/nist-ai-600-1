<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-ai-600-1

NIST AI 600-1 AI RMF Generative AI Profile (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-ai-600-1](https://lmodel.github.io/nist-ai-600-1)

## What it models

The schema renders [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) of July 2024, the Generative AI Profile of the AI Risk Management Framework (AI RMF): its 12 risks, the suggested actions its tables list under AI RMF subcategories, and its four primary considerations. It imports the base and profiles modules of [lmodel/nist-ai-100-1](https://github.com/lmodel/nist-ai-100-1), vendored in place.

`src/nist_ai_600_1/data/` holds the whole Profile as records, and `upstream/` holds the publication, pinned by hash. NIST publishes no machine-readable form, so a script reads the tables from the PDF. Tests hold the records to the publication's words and numbering, and a weekly workflow opens an issue when the file changes. [docs/about.md](docs/about.md) names the faults in the tables and what the catalogue does about each.

## Mappings

* **[lmodel/nist-ai-100-1](https://github.com/lmodel/nist-ai-100-1)**: `is_a` from the Profile to `AiRmfProfile`, and `related_mappings` from a risk, a table and an action to its risk, subcategory and suggested action. `tests/test_schema_rules.py` checks it against that repository's copy.
* **[lmodel/oscal](https://github.com/lmodel/oscal)**: `broad_mappings` from a suggested action to a part. `tests/test_schema_rules.py` checks it against the released copy.
* **[lmodel/stix](https://github.com/lmodel/stix)**: `related_mappings` from a suggested action to a course of action. `tests/test_schema_rules.py` checks it.
* **[lmodel/spdx](https://github.com/lmodel/spdx)**: `related_mappings` from the third-party control of asking for a software bill of materials to `Sbom`. `tests/test_schema_rules.py` checks it.

The schema is the one home for mappings. The hand-kept SSSOM sets are gone, since no source confirmed their rows.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the catalogue's builder and the upstream watch
* [src/nist_ai_600_1/schema/](src/nist_ai_600_1/schema): the LinkML schema, the umbrella and three modules (edit these), and the vendored modules of lmodel/nist-ai-100-1 under `nist_ai_100_1/` (do not edit them)
* [src/nist_ai_600_1/data/](src/nist_ai_600_1/data): the whole Profile as records
* [src/nist_ai_600_1/datamodel/](src/nist_ai_600_1/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [upstream/](upstream/): the publication, unchanged
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/schema/nist-ai-600-1.yaml`, is the copy `just lokf-adapt` writes from `src/nist_ai_600_1/schema/nist_ai_600_1.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-ai-600-1.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots `GaiRisk`, `GaiSubcategory`, `GaiPrimaryConsideration`, `GaiStructuredFeedback` and `AiRmfRecord` on `Concept`. In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
GaiRisk, GaiSubcategory, GaiGovernanceConsideration, GaiPreDeploymentTestingConsideration, GaiContentProvenanceConsideration, GaiIncidentDisclosureConsideration, GaiParticipatoryEngagement, GaiFieldTesting, GaiAiRedTeaming, AiRmfProfile, GaiProfile
```

The copy drops `ai_rmf_id` for LOKF's `id`, folds `title` and `description` into LOKF's, and demotes the two designators, since a concept's `type` already names its class. Every other key starts with `gai_` or `ai_rmf_`. The copy shares `AiRmfProfile` and the vendored names with lmodel/nist-ai-100-1's copy, each spelled alike, so a host importing both gets one definition of each. `tests/test_schema_rules.py` holds all this.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

NIST's works are free to reprint under its statement: see [NOTICE](NOTICE), which gives the citation. This is not a NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
