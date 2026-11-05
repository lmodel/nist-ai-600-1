# About nist-ai-600-1

This page is for anyone reading the [LinkML](https://linkml.io) schema's elements: it says how they fit together, where each part comes from and what the model leaves out.

## How the classes fit together

`GaiProfile` holds the Profile. It is an `AiRmfProfile` of the kind `cross_sectoral`, the class lmodel/nist-ai-100-1 defines for section 6 of the AI RMF.

- **`GaiRisk`** is one of the 12 risks of section 2.
- **`GaiSubcategory`** is one table of section 3. It names an AI RMF subcategory, restates it, lists `GaiSuggestedAction` records and ends with the table's AI actor tasks.
- **`GaiSuggestedAction`** is one row, with its identifier, its text and the risks it is tagged with.
- **`GaiPrimaryConsideration`** is the abstract class of the four themes of Appendix A, each with a class of its own and the lists its section gives. Pre-Deployment Testing holds the kinds of `GaiStructuredFeedback`.

Lifecycle stage, scope, source and time scale sit on `GaiRisk`, but the publication assigns none of them to a risk, since they depend on the model, system or use case. The catalogue leaves them empty for an adopter to fill.

## Where each part comes from

NIST publishes no machine-readable form of the Profile, so the publication is the only source, and `upstream/` holds it unchanged. `scripts/build_catalogue.py` reads the tables of section 3 from it. Section 2's definitions and Appendix A's lists are written by hand, and tests hold them to the publication's words.

The schema imports the base and profiles modules of lmodel/nist-ai-100-1, vendored under `src/nist_ai_600_1/schema/nist_ai_100_1/`. They give a subcategory's identifier form, the trustworthiness characteristics, the AI actor tasks and the profile.

The schema's descriptions are this project's own words. The catalogue's definitions, statements and actions are NIST's. [NOTICE](https://github.com/lmodel/nist-ai-600-1/blob/main/NOTICE) says on what terms.

## What the publication gets wrong, and what the catalogue does

The builder corrects three things in the tables and tests list each, so a change in a later edition fails a test.

- **GV4.3--001** is the first action of GOVERN 4.3, and the numbering of the actions around it shows it. The catalogue writes `GV-4.3-001`.
- **GV-1.4-002** carries the tag Civil Rights violations, which is not one of the 12 risks. The catalogue leaves that tag out.
- **One row** runs Human-AI Configuration and Dangerous, Violent, or Hateful Content together without a semicolon. The catalogue holds them as two tags.

The tables also spell some risks differently from section 2, such as Environmental for Environmental Impacts, and Harmful Bias and Homogenization for Harmful Bias or Homogenization. The enum carries the section 2 name as its title and each table spelling as an alias.

Two further faults are left as they are:

- GOVERN 1.5's restatement differs from AI 100-1's Table 1 in its wording, and a test lists it. The catalogue keeps this publication's wording.
- Section 2 says each risk is mapped to trustworthiness characteristics in section 3 and in tables in Appendix B. In fact each subsection of section 2 names them, and Appendix B holds the references. The catalogue takes them from section 2.

## Choices worth knowing

- **AI actor tasks belong to a table, not an action.** The publication says not every task listed applies to every action.
- **A risk's groupings are a list.** Footnote 5 offers them as one possible way to sort the risks, and it lists Data Privacy under all three.
- **Pre-Deployment Testing holds structured feedback.** Section A.1.7 calls those approaches part of that section, although A.1.5 has a heading of its own.

## What is left out

The schema holds none of the publication's running prose: the discussion of each risk in sections 2.1 to 2.12, or the discussion in Appendix A. It holds no definition quoted from a third party, and leaves out the references of Appendix B. The AI RMF itself is lmodel/nist-ai-100-1.

## Reference

- [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1)
- [NIST's Trustworthy and Responsible AI Resource Center](https://airc.nist.gov/Home)
- [NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1)
