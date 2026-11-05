# nist-ai-600-1

This project is a LinkML model of NIST AI 600-1, the Generative Artificial Intelligence Profile of the AI Risk Management Framework (AI RMF), which the National Institute of Standards and Technology (NIST) publishes. It holds the Profile's 12 risks, the suggested actions of its tables, and its four primary considerations. `src/nist_ai_600_1/data/ai-600-1.yaml` holds all of it as records.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the classes fit together, where each part comes from and what the model leaves out
- [`nist_ai_600_1.yaml`](schema/nist_ai_600_1.yaml): the schema, with its modules merged

## Validating a profile document

```bash
uv run linkml-validate -s src/nist_ai_600_1/schema/nist_ai_600_1.yaml -C GaiProfile src/nist_ai_600_1/data/ai-600-1.yaml
```

`project/jsonschema/nist_ai_600_1.schema.json` is the same schema for anyone without LinkML.

## What the catalogue holds

| Part | Records |
| --- | --- |
| Risks of section 2 | 12 |
| Tables of section 3, one per AI RMF subcategory | 49 |
| Suggested actions: Govern, Map, Measure and Manage | 58, 39, 72 and 43, 212 in all |
| Primary considerations of Appendix A | 4 |
| Governance plans of section A.1.2 | 25 |

`tests/test_catalogue.py` holds these counts, validates the whole file with `linkml-validate` and the committed JSON Schema, and loads it into the generated dataclasses and Pydantic models.

## What the validator does not check

JSON Schema looks at one value at a time. It does not check that an action's identifier names the subcategory it sits under, that the numbers run in order, or that each risk has an action. `tests/test_catalogue.py` checks all three. The generated Pydantic models check no pattern a type carries.
