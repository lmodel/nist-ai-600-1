"""Checks the whole catalogue against the schema and the publication.

src/nist_ai_600_1/data/ai-600-1.yaml holds the tables of section 3, which
scripts/build_catalogue.py writes from upstream/, and what section 2 and Appendix A list,
written by hand.
"""

import importlib.util
import json
import re
from functools import lru_cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

import nist_ai_600_1.datamodel.nist_ai_600_1 as dataclasses_model
import nist_ai_600_1.datamodel.nist_ai_600_1_pydantic as pydantic_model

ROOT = Path(__file__).parent.parent
CATALOGUE = ROOT / "src" / "nist_ai_600_1" / "data" / "ai-600-1.yaml"
SCHEMA = ROOT / "src" / "nist_ai_600_1" / "schema" / "nist_ai_600_1.yaml"
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "nist_ai_600_1.schema.json"
BUILDER = ROOT / "scripts" / "build_catalogue.py"
SUBCATEGORIES = Path(__file__).parent / "ai_rmf_subcategories.yaml"
PDF = ROOT / "upstream" / "NIST.AI.600-1.pdf"

FUNCTION_OF = {"GV": "GOVERN", "MP": "MAP", "MS": "MEASURE", "MG": "MANAGE"}

# Each place the publication's restatement of a subcategory differs from AI 100-1's.
RESTATED_DIFFERENTLY = {"GOVERN 1.5"}


@lru_cache(maxsize=1)
def _builder():
    spec = importlib.util.spec_from_file_location("build_catalogue", BUILDER)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@lru_cache(maxsize=1)
def _doc():
    return yaml.safe_load(CATALOGUE.read_text(encoding="utf-8"))


@lru_cache(maxsize=1)
def _view():
    return SchemaView(str(SCHEMA))


def _letters(text):
    return re.sub(r"[^a-z]", "", text.lower().translate(_builder().LIGATURES))


@lru_cache(maxsize=1)
def _publication_letters():
    """The publication's words as bare letters, so line breaks, hyphens and footnote
    marks fall away."""
    import pdfplumber

    with pdfplumber.open(PDF) as pdf:
        text = " ".join(page.extract_text() or "" for page in pdf.pages)
    return _letters(text)


def _words(text):
    """A text's words, lower-cased and each between spaces, so a title matches whole
    words and line breaks and hyphens fall away."""
    text = re.sub(r"-\n", "", text.lower().translate(_builder().LIGATURES))
    return " " + " ".join(re.findall(r"[a-z0-9]+", text)) + " "


@lru_cache(maxsize=1)
def _publication_words():
    """The publication's words."""
    import pdfplumber

    with pdfplumber.open(PDF) as pdf:
        return _words("\n".join(page.extract_text() or "" for page in pdf.pages))


def _actions():
    for record in _doc()["gai_subcategories"]:
        yield from record["gai_subcategory_actions"]


def test_catalogue_passes_the_validator():
    """`linkml-validate` passes the whole catalogue, with its format checks."""
    report = validate(_doc(), str(SCHEMA), "GaiProfile")
    assert not report.results, [r.message for r in report.results][:5]


def test_catalogue_passes_the_committed_json_schema():
    """The JSON Schema a consumer takes from project/ passes it too."""
    schema = json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))
    errors = list(jsonschema.Draft202012Validator(schema).iter_errors(_doc()))
    assert not errors, [e.message for e in errors][:5]


def test_generated_models_load_the_catalogue():
    """The generated dataclasses and Pydantic models load all of it."""
    profile = yaml_loader.load(
        str(CATALOGUE), target_class=dataclasses_model.GaiProfile
    )
    assert len(profile.gai_subcategories) == 49
    assert len(pydantic_model.GaiProfile.model_validate(_doc()).gai_subcategories) == 49


def test_tables_are_what_the_publication_gives():
    """Section 3 of the catalogue is what the builder writes from the publication."""
    assert _doc()["gai_subcategories"] == _builder().section_three()


def test_counts():
    """12 risks, 49 tables, 212 actions by function, and four considerations."""
    assert len(_doc()["gai_risks"]) == 12
    assert len(_doc()["gai_subcategories"]) == 49
    assert len(_doc()["gai_primary_considerations"]) == 4
    by_function = {}
    for action in _actions():
        prefix = action["gai_action_id"][:2]
        by_function[prefix] = by_function.get(prefix, 0) + 1
    assert by_function == {"GV": 58, "MP": 39, "MS": 72, "MG": 43}


def test_profile_is_cross_sectoral_and_lists_its_subcategories():
    """Section 1 calls it cross-sectoral, and it lists the subcategories of its tables."""
    assert _doc()["ai_rmf_profile_kinds"] == ["cross_sectoral"]
    assert _doc()["ai_rmf_profile_subcategories"] == [
        record["ai_rmf_subcategory_id"] for record in _doc()["gai_subcategories"]
    ]


def test_action_identifiers_name_their_subcategory_and_run_in_order():
    """GV-1.1-002 is the second action of GOVERN 1.1, as the publication says."""
    for record in _doc()["gai_subcategories"]:
        for number, action in enumerate(record["gai_subcategory_actions"], 1):
            prefix, sub, seq = action["gai_action_id"].split("-")
            assert f"{FUNCTION_OF[prefix]} {sub}" == record["ai_rmf_subcategory_id"]
            assert int(seq) == number, action["gai_action_id"]


def test_each_table_has_its_actor_tasks():
    """Every table ends with its AI actor tasks."""
    for record in _doc()["gai_subcategories"]:
        assert record.get("gai_subcategory_actor_tasks"), record[
            "ai_rmf_subcategory_id"
        ]


def test_each_action_has_risks_and_each_risk_an_action():
    """Each row carries a tag, and each of the 12 risks tags at least one action."""
    used = set()
    for action in _actions():
        assert action.get("gai_action_risks"), action["gai_action_id"]
        used.update(action["gai_action_risks"])
    assert used == set(_view().get_enum("GaiRiskName").permissible_values)


def test_corrections_to_the_tables_are_the_listed_ones():
    """The builder corrects only what the module lists. Each list's entry is real."""
    builder = _builder()
    rows = builder.table_rows()
    firsts = [builder.text_of(cells[0]) for cells in rows]
    assert builder.ID_TYPOS == {"GV4.3--001": "GV-4.3-001"}
    assert "GV4.3--001" in firsts
    tags = [builder.text_of(cells[2]) for cells in rows if len(cells) > 2]
    assert any("Civil Rights violations" in tag for tag in tags)
    for joined in builder.JOINED_TAGS:
        assert any(joined in tag for tag in tags)


def test_subcategories_are_the_ai_rmfs():
    """Each table names a subcategory of AI 100-1 and restates it, but for those listed."""
    statements = yaml.safe_load(SUBCATEGORIES.read_text(encoding="utf-8"))
    assert len(statements) == 72
    differing = set()
    for record in _doc()["gai_subcategories"]:
        name = record["ai_rmf_subcategory_id"]
        if _letters(statements[name]) != _letters(record["description"]):
            differing.add(name)
    assert differing == RESTATED_DIFFERENTLY


def test_risks_follow_the_publication():
    """The records follow section 2's order and each enum value has one."""
    names = [r["gai_risk_name"] for r in _doc()["gai_risks"]]
    assert names == list(_view().get_enum("GaiRiskName").permissible_values)
    assert [r["gai_risk_section"] for r in _doc()["gai_risks"]] == [
        f"2.{n}" for n in range(1, 13)
    ]


def test_risk_definitions_are_the_publications():
    """Each definition is the publication's words. A page break splits one of them."""
    letters = _publication_letters()
    for risk in _doc()["gai_risks"]:
        text = risk["description"]
        if risk["gai_risk_name"] == "information_security":
            head, tail = text.split("offensive cyber operations")
            assert _letters(head) + _letters("offensive cyber") in letters
            assert _letters("operations" + tail) in letters
        else:
            assert _letters(text) in letters, risk["gai_risk_name"]


def test_footnote_five_lists_data_privacy_under_all_three_groups():
    """The groupings are many-valued because footnote 5 says so."""
    privacy = next(
        r for r in _doc()["gai_risks"] if r["gai_risk_name"] == "data_privacy"
    )
    assert set(privacy["gai_risk_groupings"]) == set(
        _view().get_enum("GaiRiskGrouping").permissible_values
    )


@pytest.mark.parametrize(
    "enum",
    [
        "GaiRiskName",
        "GaiRiskGrouping",
        "GaiRedTeamingType",
        "GaiProvenanceTechnique",
    ],
)
def test_titles_are_the_publications(enum):
    """Each title is the publication's wording, so a typing slip fails here."""
    words = _publication_words()
    for value, entry in _view().get_enum(enum).permissible_values.items():
        assert _words(entry.title) in words, (enum, value)


def test_governance_plans_are_the_publications():
    """Section A.1.2 sets the plans in two columns, so a wrapped title is not contiguous
    in the page's text. Each of its words must still be there."""
    letters = _publication_letters()
    for value, entry in (
        _view().get_enum("GaiGovernancePlan").permissible_values.items()
    ):
        for word in entry.title.split():
            assert _letters(word) in letters, (value, word)


def test_lists_of_appendix_a_are_complete():
    """25 plans, 4 techniques, 4 types of red-teaming and 3 kinds of feedback."""
    records = {
        r["gai_consideration_type"]: r for r in _doc()["gai_primary_considerations"]
    }
    governance = records["GaiGovernanceConsideration"]
    assert len(set(governance["gai_governance_plans"])) == 25
    assert len(governance["gai_third_party_controls"]) == 4
    provenance = records["GaiContentProvenanceConsideration"]
    assert len(provenance["gai_provenance_techniques"]) == 4
    testing = records["GaiPreDeploymentTestingConsideration"]
    assert len(testing["gai_structured_feedback"]) == 3
    assert len(records["GaiIncidentDisclosureConsideration"]["gai_incident_harms"]) == 4
