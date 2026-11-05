# Auto generated from nist_ai_600_1.yaml by pythongen.py version: 0.0.1
# Schema: nist_ai_600_1
#
# id: https://w3id.org/lmodel/nist-ai-600-1
# description: A LinkML model of NIST AI 600-1, the Generative Artificial Intelligence Profile of the AI Risk Management Framework: its 12 risks, the suggested actions its tables list under AI RMF subcategories, and its four primary considerations.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.12.0"
version = "1.0.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_AI_100_1 = CurieNamespace('nist_ai_100_1', 'https://w3id.org/lmodel/nist-ai-100-1/')
NIST_AI_600_1 = CurieNamespace('nist_ai_600_1', 'https://w3id.org/lmodel/nist-ai-600-1/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_AI_600_1


# Types
class AiRmfFunctionIdentifier(String):
    """ The name of one of the four Core functions, written in capitals, such as GOVERN. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_function_identifier"
    type_model_uri = NIST_AI_600_1.AiRmfFunctionIdentifier


class AiRmfCategoryIdentifier(String):
    """ A category's identifier, its function's name and a number, such as GOVERN 1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_category_identifier"
    type_model_uri = NIST_AI_600_1.AiRmfCategoryIdentifier


class AiRmfSubcategoryIdentifier(String):
    """ A subcategory's identifier, its category's identifier, a dot and a number, such as GOVERN 1.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_subcategory_identifier"
    type_model_uri = NIST_AI_600_1.AiRmfSubcategoryIdentifier


class GaiActionIdentifier(String):
    """ An Action ID: the function's two letters, its subcategory's numbers and a three-digit number, such as GV-1.1-001 for the first action of GOVERN 1.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "gai_action_identifier"
    type_model_uri = NIST_AI_600_1.GaiActionIdentifier


# Class references
class AiRmfRecordAiRmfId(URIorCURIE):
    pass


class AiRmfProfileAiRmfId(AiRmfRecordAiRmfId):
    pass


class GaiProfileAiRmfId(AiRmfProfileAiRmfId):
    pass


@dataclass(repr=False)
class AiRmfRecord(YAMLRoot):
    """
    The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct
    from what the publication itself lists.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Record"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Record"
    class_name: ClassVar[str] = "AiRmfRecord"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.AiRmfRecord

    ai_rmf_id: Union[str, AiRmfRecordAiRmfId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfRecordAiRmfId):
            self.ai_rmf_id = AiRmfRecordAiRmfId(self.ai_rmf_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfProfile(AiRmfRecord):
    """
    An implementation of the Core's functions, categories and subcategories for a setting, application or technology,
    based on the adopter's requirements, risk tolerance and resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Profile"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Profile"
    class_name: ClassVar[str] = "AiRmfProfile"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.AiRmfProfile

    ai_rmf_id: Union[str, AiRmfProfileAiRmfId] = None
    ai_rmf_profile_kinds: Union[Union[str, "AiRmfProfileKind"], list[Union[str, "AiRmfProfileKind"]]] = None
    ai_rmf_profile_setting: Optional[str] = None
    ai_rmf_profile_subcategories: Optional[Union[Union[str, AiRmfSubcategoryIdentifier], list[Union[str, AiRmfSubcategoryIdentifier]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfProfileAiRmfId):
            self.ai_rmf_id = AiRmfProfileAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.ai_rmf_profile_kinds):
            self.MissingRequiredField("ai_rmf_profile_kinds")
        if not isinstance(self.ai_rmf_profile_kinds, list):
            self.ai_rmf_profile_kinds = [self.ai_rmf_profile_kinds] if self.ai_rmf_profile_kinds is not None else []
        self.ai_rmf_profile_kinds = [v if isinstance(v, AiRmfProfileKind) else AiRmfProfileKind(v) for v in self.ai_rmf_profile_kinds]

        if self.ai_rmf_profile_setting is not None and not isinstance(self.ai_rmf_profile_setting, str):
            self.ai_rmf_profile_setting = str(self.ai_rmf_profile_setting)

        if not isinstance(self.ai_rmf_profile_subcategories, list):
            self.ai_rmf_profile_subcategories = [self.ai_rmf_profile_subcategories] if self.ai_rmf_profile_subcategories is not None else []
        self.ai_rmf_profile_subcategories = [v if isinstance(v, AiRmfSubcategoryIdentifier) else AiRmfSubcategoryIdentifier(v) for v in self.ai_rmf_profile_subcategories]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiProfile(AiRmfProfile):
    """
    The Generative AI Profile as a whole, a cross-sectoral profile of the AI RMF and a companion resource to it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["Profile"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:Profile"
    class_name: ClassVar[str] = "GaiProfile"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiProfile

    ai_rmf_id: Union[str, GaiProfileAiRmfId] = None
    ai_rmf_profile_kinds: Union[Union[str, "AiRmfProfileKind"], list[Union[str, "AiRmfProfileKind"]]] = None
    gai_risks: Union[Union[dict, "GaiRisk"], list[Union[dict, "GaiRisk"]]] = None
    gai_subcategories: Union[Union[dict, "GaiSubcategory"], list[Union[dict, "GaiSubcategory"]]] = None
    gai_primary_considerations: Optional[Union[Union[dict, "GaiPrimaryConsideration"], list[Union[dict, "GaiPrimaryConsideration"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, GaiProfileAiRmfId):
            self.ai_rmf_id = GaiProfileAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.gai_risks):
            self.MissingRequiredField("gai_risks")
        self._normalize_inlined_as_list(slot_name="gai_risks", slot_type=GaiRisk, key_name="gai_risk_name", keyed=False)

        if self._is_empty(self.gai_subcategories):
            self.MissingRequiredField("gai_subcategories")
        self._normalize_inlined_as_list(slot_name="gai_subcategories", slot_type=GaiSubcategory, key_name="ai_rmf_subcategory_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="gai_primary_considerations", slot_type=GaiPrimaryConsideration, key_name="gai_consideration_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiRisk(YAMLRoot):
    """
    A risk that section 2 defines as unique to or made worse by the development and use of GAI.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["Risk"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:Risk"
    class_name: ClassVar[str] = "GaiRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiRisk

    gai_risk_name: Union[str, "GaiRiskName"] = None
    gai_risk_section: str = None
    description: Optional[str] = None
    gai_risk_characteristics: Optional[Union[Union[str, "AiRmfCharacteristicName"], list[Union[str, "AiRmfCharacteristicName"]]]] = empty_list()
    gai_risk_groupings: Optional[Union[Union[str, "GaiRiskGrouping"], list[Union[str, "GaiRiskGrouping"]]]] = empty_list()
    gai_risk_lifecycle_stages: Optional[Union[Union[str, "GaiLifecycleStage"], list[Union[str, "GaiLifecycleStage"]]]] = empty_list()
    gai_risk_scopes: Optional[Union[Union[str, "GaiRiskScope"], list[Union[str, "GaiRiskScope"]]]] = empty_list()
    gai_risk_sources: Optional[Union[Union[str, "GaiRiskSource"], list[Union[str, "GaiRiskSource"]]]] = empty_list()
    gai_risk_time_scales: Optional[Union[Union[str, "GaiRiskTimeScale"], list[Union[str, "GaiRiskTimeScale"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gai_risk_name):
            self.MissingRequiredField("gai_risk_name")
        if not isinstance(self.gai_risk_name, GaiRiskName):
            self.gai_risk_name = GaiRiskName(self.gai_risk_name)

        if self._is_empty(self.gai_risk_section):
            self.MissingRequiredField("gai_risk_section")
        if not isinstance(self.gai_risk_section, str):
            self.gai_risk_section = str(self.gai_risk_section)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.gai_risk_characteristics, list):
            self.gai_risk_characteristics = [self.gai_risk_characteristics] if self.gai_risk_characteristics is not None else []
        self.gai_risk_characteristics = [v if isinstance(v, AiRmfCharacteristicName) else AiRmfCharacteristicName(v) for v in self.gai_risk_characteristics]

        if not isinstance(self.gai_risk_groupings, list):
            self.gai_risk_groupings = [self.gai_risk_groupings] if self.gai_risk_groupings is not None else []
        self.gai_risk_groupings = [v if isinstance(v, GaiRiskGrouping) else GaiRiskGrouping(v) for v in self.gai_risk_groupings]

        if not isinstance(self.gai_risk_lifecycle_stages, list):
            self.gai_risk_lifecycle_stages = [self.gai_risk_lifecycle_stages] if self.gai_risk_lifecycle_stages is not None else []
        self.gai_risk_lifecycle_stages = [v if isinstance(v, GaiLifecycleStage) else GaiLifecycleStage(v) for v in self.gai_risk_lifecycle_stages]

        if not isinstance(self.gai_risk_scopes, list):
            self.gai_risk_scopes = [self.gai_risk_scopes] if self.gai_risk_scopes is not None else []
        self.gai_risk_scopes = [v if isinstance(v, GaiRiskScope) else GaiRiskScope(v) for v in self.gai_risk_scopes]

        if not isinstance(self.gai_risk_sources, list):
            self.gai_risk_sources = [self.gai_risk_sources] if self.gai_risk_sources is not None else []
        self.gai_risk_sources = [v if isinstance(v, GaiRiskSource) else GaiRiskSource(v) for v in self.gai_risk_sources]

        if not isinstance(self.gai_risk_time_scales, list):
            self.gai_risk_time_scales = [self.gai_risk_time_scales] if self.gai_risk_time_scales is not None else []
        self.gai_risk_time_scales = [v if isinstance(v, GaiRiskTimeScale) else GaiRiskTimeScale(v) for v in self.gai_risk_time_scales]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiSubcategory(YAMLRoot):
    """
    An AI RMF subcategory as one table of section 3 addresses it. The Profile covers only some of the 72.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["Subcategory"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:Subcategory"
    class_name: ClassVar[str] = "GaiSubcategory"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiSubcategory

    ai_rmf_subcategory_id: Union[str, AiRmfSubcategoryIdentifier] = None
    description: str = None
    gai_subcategory_actions: Union[Union[dict, "GaiSuggestedAction"], list[Union[dict, "GaiSuggestedAction"]]] = None
    gai_subcategory_actor_tasks: Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_subcategory_id):
            self.MissingRequiredField("ai_rmf_subcategory_id")
        if not isinstance(self.ai_rmf_subcategory_id, AiRmfSubcategoryIdentifier):
            self.ai_rmf_subcategory_id = AiRmfSubcategoryIdentifier(self.ai_rmf_subcategory_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.gai_subcategory_actions):
            self.MissingRequiredField("gai_subcategory_actions")
        self._normalize_inlined_as_list(slot_name="gai_subcategory_actions", slot_type=GaiSuggestedAction, key_name="gai_action_id", keyed=False)

        if not isinstance(self.gai_subcategory_actor_tasks, list):
            self.gai_subcategory_actor_tasks = [self.gai_subcategory_actor_tasks] if self.gai_subcategory_actor_tasks is not None else []
        self.gai_subcategory_actor_tasks = [v if isinstance(v, AiRmfActorTaskName) else AiRmfActorTaskName(v) for v in self.gai_subcategory_actor_tasks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiSuggestedAction(YAMLRoot):
    """
    A step an organization or AI actor can take to manage GAI risks, which one row of a table states.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["SuggestedAction"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:SuggestedAction"
    class_name: ClassVar[str] = "GaiSuggestedAction"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiSuggestedAction

    gai_action_id: Union[str, GaiActionIdentifier] = None
    description: str = None
    gai_action_risks: Optional[Union[Union[str, "GaiRiskName"], list[Union[str, "GaiRiskName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gai_action_id):
            self.MissingRequiredField("gai_action_id")
        if not isinstance(self.gai_action_id, GaiActionIdentifier):
            self.gai_action_id = GaiActionIdentifier(self.gai_action_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.gai_action_risks, list):
            self.gai_action_risks = [self.gai_action_risks] if self.gai_action_risks is not None else []
        self.gai_action_risks = [v if isinstance(v, GaiRiskName) else GaiRiskName(v) for v in self.gai_action_risks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiPrimaryConsideration(YAMLRoot):
    """
    One of the four primary considerations of Appendix A, which also inform the suggested actions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["PrimaryConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:PrimaryConsideration"
    class_name: ClassVar[str] = "GaiPrimaryConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiPrimaryConsideration

    gai_consideration_type: str = None
    title: str = None
    description: Optional[str] = None
    gai_consideration_sections: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.gai_consideration_sections, list):
            self.gai_consideration_sections = [self.gai_consideration_sections] if self.gai_consideration_sections is not None else []
        self.gai_consideration_sections = [v if isinstance(v, str) else str(v) for v in self.gai_consideration_sections]

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "gai_consideration_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class GaiGovernanceConsideration(GaiPrimaryConsideration):
    """
    How an organization's governance can be revisited for GAI, including across the AI value chain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["GovernanceConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:GovernanceConsideration"
    class_name: ClassVar[str] = "GaiGovernanceConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiGovernanceConsideration

    gai_consideration_type: str = None
    title: str = None
    gai_governance_plans: Optional[Union[Union[str, "GaiGovernancePlan"], list[Union[str, "GaiGovernancePlan"]]]] = empty_list()
    gai_third_party_controls: Optional[Union[Union[str, "GaiThirdPartyControl"], list[Union[str, "GaiThirdPartyControl"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gai_governance_plans, list):
            self.gai_governance_plans = [self.gai_governance_plans] if self.gai_governance_plans is not None else []
        self.gai_governance_plans = [v if isinstance(v, GaiGovernancePlan) else GaiGovernancePlan(v) for v in self.gai_governance_plans]

        if not isinstance(self.gai_third_party_controls, list):
            self.gai_third_party_controls = [self.gai_third_party_controls] if self.gai_third_party_controls is not None else []
        self.gai_third_party_controls = [v if isinstance(v, GaiThirdPartyControl) else GaiThirdPartyControl(v) for v in self.gai_third_party_controls]

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)


@dataclass(repr=False)
class GaiPreDeploymentTestingConsideration(GaiPrimaryConsideration):
    """
    How GAI can be tested before deployment while better approaches mature, and where current tests fall short.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["PreDeploymentTestingConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:PreDeploymentTestingConsideration"
    class_name: ClassVar[str] = "GaiPreDeploymentTestingConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiPreDeploymentTestingConsideration

    gai_consideration_type: str = None
    title: str = None
    gai_structured_feedback: Optional[Union[Union[dict, "GaiStructuredFeedback"], list[Union[dict, "GaiStructuredFeedback"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="gai_structured_feedback", slot_type=GaiStructuredFeedback, key_name="gai_feedback_type", keyed=False)

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)


@dataclass(repr=False)
class GaiContentProvenanceConsideration(GaiPrimaryConsideration):
    """
    How tracking the origin and history of content helps tell authentic content from synthetic content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["ContentProvenanceConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:ContentProvenanceConsideration"
    class_name: ClassVar[str] = "GaiContentProvenanceConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiContentProvenanceConsideration

    gai_consideration_type: str = None
    title: str = None
    gai_provenance_techniques: Optional[Union[Union[str, "GaiProvenanceTechnique"], list[Union[str, "GaiProvenanceTechnique"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gai_provenance_techniques, list):
            self.gai_provenance_techniques = [self.gai_provenance_techniques] if self.gai_provenance_techniques is not None else []
        self.gai_provenance_techniques = [v if isinstance(v, GaiProvenanceTechnique) else GaiProvenanceTechnique(v) for v in self.gai_provenance_techniques]

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)


@dataclass(repr=False)
class GaiIncidentDisclosureConsideration(GaiPrimaryConsideration):
    """
    How documenting, reporting and sharing AI incidents helps prevent harm, though no formal channels exist.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["IncidentDisclosureConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:IncidentDisclosureConsideration"
    class_name: ClassVar[str] = "GaiIncidentDisclosureConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiIncidentDisclosureConsideration

    gai_consideration_type: str = None
    title: str = None
    gai_incident_harms: Optional[Union[Union[str, "GaiIncidentHarm"], list[Union[str, "GaiIncidentHarm"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gai_incident_harms, list):
            self.gai_incident_harms = [self.gai_incident_harms] if self.gai_incident_harms is not None else []
        self.gai_incident_harms = [v if isinstance(v, GaiIncidentHarm) else GaiIncidentHarm(v) for v in self.gai_incident_harms]

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)


@dataclass(repr=False)
class GaiStructuredFeedback(YAMLRoot):
    """
    A way of using structured public feedback to evaluate whether GAI systems perform as intended.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["StructuredFeedback"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:StructuredFeedback"
    class_name: ClassVar[str] = "GaiStructuredFeedback"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiStructuredFeedback

    gai_feedback_type: str = None
    title: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gai_feedback_type):
            self.MissingRequiredField("gai_feedback_type")
        self.gai_feedback_type = str(self.class_name)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "gai_feedback_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class GaiParticipatoryEngagement(GaiStructuredFeedback):
    """
    Asking civil society groups, affected communities and users for feedback, such as through focus groups or surveys.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["ParticipatoryEngagement"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:ParticipatoryEngagement"
    class_name: ClassVar[str] = "GaiParticipatoryEngagement"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiParticipatoryEngagement

    gai_feedback_type: str = None
    title: str = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_feedback_type):
            self.MissingRequiredField("gai_feedback_type")
        self.gai_feedback_type = str(self.class_name)


@dataclass(repr=False)
class GaiFieldTesting(GaiStructuredFeedback):
    """
    Structured settings that show how people interact with and use AI-generated information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["FieldTesting"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:FieldTesting"
    class_name: ClassVar[str] = "GaiFieldTesting"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiFieldTesting

    gai_feedback_type: str = None
    title: str = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_feedback_type):
            self.MissingRequiredField("gai_feedback_type")
        self.gai_feedback_type = str(self.class_name)


@dataclass(repr=False)
class GaiAiRedTeaming(GaiStructuredFeedback):
    """
    A structured exercise that probes an AI system for flaws and vulnerabilities, often with its developers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["AiRedTeaming"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:AiRedTeaming"
    class_name: ClassVar[str] = "GaiAiRedTeaming"
    class_model_uri: ClassVar[URIRef] = NIST_AI_600_1.GaiAiRedTeaming

    gai_feedback_type: str = None
    title: str = None
    gai_red_teaming_types: Optional[Union[Union[str, "GaiRedTeamingType"], list[Union[str, "GaiRedTeamingType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gai_red_teaming_types, list):
            self.gai_red_teaming_types = [self.gai_red_teaming_types] if self.gai_red_teaming_types is not None else []
        self.gai_red_teaming_types = [v if isinstance(v, GaiRedTeamingType) else GaiRedTeamingType(v) for v in self.gai_red_teaming_types]

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_feedback_type):
            self.MissingRequiredField("gai_feedback_type")
        self.gai_feedback_type = str(self.class_name)


# Enumerations
class AiRmfCharacteristicName(EnumDefinitionImpl):
    """
    The seven characteristics of trustworthy AI systems in section 3 of the publication.
    """
    valid_and_reliable = PermissibleValue(
        text="valid_and_reliable",
        title="Valid and Reliable",
        description="""Shown by evidence to meet the needs of its intended use, and works without failure over time. Figure 4 makes it a necessary condition for the others.""")
    safe = PermissibleValue(
        text="safe",
        title="Safe",
        description="Keeps people, property and the environment out of danger under defined conditions.")
    secure_and_resilient = PermissibleValue(
        text="secure_and_resilient",
        title="Secure and Resilient",
        description="""Withstands adverse events and recovers from them, and keeps confidentiality, integrity and availability through protections against attack.""")
    accountable_and_transparent = PermissibleValue(
        text="accountable_and_transparent",
        title="Accountable and Transparent",
        description="""Answerable for outcomes, which rests on people being able to get information about the system and its outputs. Figure 4 shows it relating to all the others.""")
    explainable_and_interpretable = PermissibleValue(
        text="explainable_and_interpretable",
        title="Explainable and Interpretable",
        description="""Its working can be represented (how a decision was made) and its output understood in context (why, and what it means for the user).""")
    privacy_enhanced = PermissibleValue(
        text="privacy_enhanced",
        title="Privacy-Enhanced",
        description="""Guided by the norms and practices that protect human autonomy, identity and dignity, such as anonymity, confidentiality and control.""")
    fair_with_harmful_bias_managed = PermissibleValue(
        text="fair_with_harmful_bias_managed",
        title="Fair – with Harmful Bias Managed",
        description="""Addresses equality and equity, including harmful bias and discrimination, knowing that views of fairness differ across cultures and applications.""")

    _defn = EnumDefinition(
        name="AiRmfCharacteristicName",
        description="The seven characteristics of trustworthy AI systems in section 3 of the publication.",
    )

class AiRmfActorTaskName(EnumDefinitionImpl):
    """
    The ten AI actor tasks and five additional AI actors of Appendix A.
    """
    ai_design = PermissibleValue(
        text="ai_design",
        title="AI Design",
        description="""Setting what the system is for, planning and designing it, and gathering and preparing its data.""")
    ai_development = PermissibleValue(
        text="ai_development",
        title="AI Development",
        description="""Providing the initial infrastructure, and creating, selecting, calibrating, training and testing models.""")
    ai_deployment = PermissibleValue(
        text="ai_deployment",
        title="AI Deployment",
        description="""Deciding how the system is used and putting it into production, including pilots and compliance checks.""")
    operation_and_monitoring = PermissibleValue(
        text="operation_and_monitoring",
        title="Operation and Monitoring",
        description="Running the system and regularly assessing its output and impacts.")
    tevv = PermissibleValue(
        text="tevv",
        title="Test, Evaluation, Verification, and Validation (TEVV)",
        description="""Examining the system or its components and finding and fixing problems, throughout the lifecycle.""")
    human_factors = PermissibleValue(
        text="human_factors",
        title="Human Factors",
        description="""Human-centered design and evaluation, involving end users and bringing context-specific norms and values into design.""")
    domain_expert = PermissibleValue(
        text="domain_expert",
        title="Domain Expert",
        description="Giving knowledge of the sector or setting where the system is used.")
    ai_impact_assessment = PermissibleValue(
        text="ai_impact_assessment",
        title="AI Impact Assessment",
        description="Assessing accountability, harmful bias, impacts, product safety, liability and security.")
    procurement = PermissibleValue(
        text="procurement",
        title="Procurement",
        description="Buying AI from another party, under financial, legal or policy authority.")
    governance_and_oversight = PermissibleValue(
        text="governance_and_oversight",
        title="Governance and Oversight",
        description="""Holding management, fiduciary and legal authority for the organization where the system is designed, developed or deployed.""")
    third_party_entities = PermissibleValue(
        text="third_party_entities",
        title="Third-party entities",
        description="""Outside organizations that supply or evaluate the data, models, systems or services an organization acquires.""")
    end_users = PermissibleValue(
        text="end_users",
        title="End users",
        description="The people or groups who use the system, whether new to technology or expert in AI.")
    affected_individuals_and_communities = PermissibleValue(
        text="affected_individuals_and_communities",
        title="Affected individuals/communities",
        description="""Those directly or indirectly affected by the system or its output, whether or not they interact with it.""")
    other_ai_actors = PermissibleValue(
        text="other_ai_actors",
        title="Other AI actors",
        description="""Those who set norms or guidance on AI risk, such as standards bodies, advocacy groups and researchers.""")
    general_public = PermissibleValue(
        text="general_public",
        title="General public",
        description="""Those most likely to experience the impacts directly, who may motivate what other AI actors do.""")

    _defn = EnumDefinition(
        name="AiRmfActorTaskName",
        description="The ten AI actor tasks and five additional AI actors of Appendix A.",
    )

class AiRmfProfileKind(EnumDefinitionImpl):
    """
    The kinds of AI RMF profile that section 6 names.
    """
    use_case = PermissibleValue(
        text="use_case",
        title="Use-case profile",
        description="The Core implemented for a specific setting or application.")
    current = PermissibleValue(
        text="current",
        title="Current Profile",
        description="""A temporal profile saying how AI is managed today and the related risks, in terms of current outcomes.""")
    target = PermissibleValue(
        text="target",
        title="Target Profile",
        description="A temporal profile saying which outcomes the desired risk management goals need.")
    cross_sectoral = PermissibleValue(
        text="cross_sectoral",
        title="Cross-sectoral profile",
        description="""Covers risks of models or applications used across use cases or sectors, or activities common to them, such as using large language models.""")

    _defn = EnumDefinition(
        name="AiRmfProfileKind",
        description="The kinds of AI RMF profile that section 6 names.",
    )

class GaiRiskName(EnumDefinitionImpl):
    """
    The 12 risks of section 2.
    """
    cbrn_information_or_capabilities = PermissibleValue(
        text="cbrn_information_or_capabilities",
        title="CBRN Information or Capabilities",
        description="""Easier access to dangerous information or design abilities for chemical, biological, radiological or nuclear weapons.""")
    confabulation = PermissibleValue(
        text="confabulation",
        title="Confabulation",
        description="Confident but wrong output that can mislead users.")
    dangerous_violent_or_hateful_content = PermissibleValue(
        text="dangerous_violent_or_hateful_content",
        title="Dangerous, Violent, or Hateful Content",
        description="Easier production of content that incites or threatens, recommends harm, or disparages.")
    data_privacy = PermissibleValue(
        text="data_privacy",
        title="Data Privacy",
        description="Leaks, misuse or de-anonymization of personal or sensitive data.")
    environmental_impacts = PermissibleValue(
        text="environmental_impacts",
        title="Environmental Impacts",
        description="Effects on ecosystems from the heavy computing that training and operating models need.")
    harmful_bias_or_homogenization = PermissibleValue(
        text="harmful_bias_or_homogenization",
        title="Harmful Bias or Homogenization",
        description="""Worse systemic bias, unequal performance across groups or languages, and output skewed by sameness.""")
    human_ai_configuration = PermissibleValue(
        text="human_ai_configuration",
        title="Human-AI Configuration",
        description="""Interaction that leads people to over-rely on, anthropomorphize or become entangled with a system, or to distrust it.""")
    information_integrity = PermissibleValue(
        text="information_integrity",
        title="Information Integrity",
        description="""Easier creation and spread of content that blurs fact and opinion, or that can drive large disinformation campaigns.""")
    information_security = PermissibleValue(
        text="information_security",
        title="Information Security",
        description="""Easier offensive cyber activity, and a larger attack surface on a system, its data, code or weights.""")
    intellectual_property = PermissibleValue(
        text="intellectual_property",
        title="Intellectual Property",
        description="Easier unauthorized copying of protected content, exposure of trade secrets, and plagiarism.")
    obscene_degrading_or_abusive_content = PermissibleValue(
        text="obscene_degrading_or_abusive_content",
        title="Obscene, Degrading, and/or Abusive Content",
        description="""Easier production of harmful imagery, including synthetic abuse material and intimate images without consent.""")
    value_chain_and_component_integration = PermissibleValue(
        text="value_chain_and_component_integration",
        title="Value Chain and Component Integration",
        description="""Opaque use of third-party components and data, and poor supplier vetting, that weaken accountability downstream.""")

    _defn = EnumDefinition(
        name="GaiRiskName",
        description="The 12 risks of section 2.",
    )

class GaiRiskGrouping(EnumDefinitionImpl):
    """
    The three groups into which footnote 5 says an organization could sort the risks, as one possible way.
    """
    technical_or_model = PermissibleValue(
        text="technical_or_model",
        title="Technical / Model risks",
        description="Risks from malfunction.")
    misuse_by_humans = PermissibleValue(
        text="misuse_by_humans",
        title="Misuse by humans",
        description="Risks from malicious use.")
    ecosystem_or_societal = PermissibleValue(
        text="ecosystem_or_societal",
        title="Ecosystem / societal risks",
        description="Systemic risks.")

    _defn = EnumDefinition(
        name="GaiRiskGrouping",
        description="""The three groups into which footnote 5 says an organization could sort the risks, as one possible way.""",
    )

class GaiLifecycleStage(EnumDefinitionImpl):
    """
    The lifecycle stages section 2 names for GAI. They differ from the seven stages of the AI RMF's Figure 3.
    """
    design = PermissibleValue(
        text="design",
        title="Design",
        description="Setting out the system before it is built.")
    development = PermissibleValue(
        text="development",
        title="Development",
        description="Building and training it.")
    deployment = PermissibleValue(
        text="deployment",
        title="Deployment",
        description="Putting it into use.")
    operation = PermissibleValue(
        text="operation",
        title="Operation",
        description="Running it.")
    decommissioning = PermissibleValue(
        text="decommissioning",
        title="Decommissioning",
        description="Retiring it.")

    _defn = EnumDefinition(
        name="GaiLifecycleStage",
        description="""The lifecycle stages section 2 names for GAI. They differ from the seven stages of the AI RMF's Figure 3.""",
    )

class GaiRiskScope(EnumDefinitionImpl):
    """
    The levels where section 2 says a risk may exist.
    """
    model_or_system = PermissibleValue(
        text="model_or_system",
        title="Model or system",
        description="The level of one model or system.")
    application_or_implementation = PermissibleValue(
        text="application_or_implementation",
        title="Application or implementation",
        description="The level of one specific use case.")
    ecosystem = PermissibleValue(
        text="ecosystem",
        title="Ecosystem",
        description="""Beyond one system or organization, such as algorithmic monocultures or effects on labor markets.""")

    _defn = EnumDefinition(
        name="GaiRiskScope",
        description="The levels where section 2 says a risk may exist.",
    )

class GaiRiskSource(EnumDefinitionImpl):
    """
    Where section 2 says a risk may come from.
    """
    design = PermissibleValue(
        text="design",
        title="Design",
        description="The design of the model itself.")
    training = PermissibleValue(
        text="training",
        title="Training",
        description="The training of the model.")
    operation = PermissibleValue(
        text="operation",
        title="Operation",
        description="The operation of the model.")
    inputs = PermissibleValue(
        text="inputs",
        title="Inputs",
        description="What goes into the model or system.")
    outputs = PermissibleValue(
        text="outputs",
        title="Outputs",
        description="What the system produces.")
    human_behavior = PermissibleValue(
        text="human_behavior",
        title="Human behavior",
        description="Abuse, misuse or unsafe repurposing by people, whether adversarial or not.")
    human_ai_interaction = PermissibleValue(
        text="human_ai_interaction",
        title="Human-AI interaction",
        description="How a person and a system act on each other.")

    _defn = EnumDefinition(
        name="GaiRiskSource",
        description="Where section 2 says a risk may come from.",
    )

class GaiRiskTimeScale(EnumDefinitionImpl):
    """
    How section 2 says a risk may materialize over time.
    """
    abrupt = PermissibleValue(
        text="abrupt",
        title="Abruptly",
        description="All at once, such as immediate emotional harm from a harmful deepfake image.")
    extended = PermissibleValue(
        text="extended",
        title="Across extended periods",
        description="Slowly, such as the long-term effect of disinformation on trust in institutions.")

    _defn = EnumDefinition(
        name="GaiRiskTimeScale",
        description="How section 2 says a risk may materialize over time.",
    )

class GaiGovernancePlan(EnumDefinitionImpl):
    """
    The plans and actions that section A.1.2 says apply to GAI from other AI governance.
    """
    accessibility_and_reasonable_accommodations = PermissibleValue(
        text="accessibility_and_reasonable_accommodations",
        title="Accessibility and reasonable accommodations")
    ai_actor_credentials_and_qualifications = PermissibleValue(
        text="ai_actor_credentials_and_qualifications",
        title="AI actor credentials and qualifications")
    alignment_to_organizational_values = PermissibleValue(
        text="alignment_to_organizational_values",
        title="Alignment to organizational values")
    auditing_and_assessment = PermissibleValue(
        text="auditing_and_assessment",
        title="Auditing and assessment")
    change_management_controls = PermissibleValue(
        text="change_management_controls",
        title="Change-management controls")
    commercial_use = PermissibleValue(
        text="commercial_use",
        title="Commercial use")
    data_provenance = PermissibleValue(
        text="data_provenance",
        title="Data provenance")
    data_protection = PermissibleValue(
        text="data_protection",
        title="Data protection")
    data_retention = PermissibleValue(
        text="data_retention",
        title="Data retention")
    consistency_in_use_of_defining_key_terms = PermissibleValue(
        text="consistency_in_use_of_defining_key_terms",
        title="Consistency in use of defining key terms")
    decommissioning = PermissibleValue(
        text="decommissioning",
        title="Decommissioning")
    discouraging_anonymous_use = PermissibleValue(
        text="discouraging_anonymous_use",
        title="Discouraging anonymous use")
    education = PermissibleValue(
        text="education",
        title="Education")
    impact_assessments = PermissibleValue(
        text="impact_assessments",
        title="Impact assessments")
    incident_response = PermissibleValue(
        text="incident_response",
        title="Incident response")
    monitoring = PermissibleValue(
        text="monitoring",
        title="Monitoring")
    opt_outs = PermissibleValue(
        text="opt_outs",
        title="Opt-outs")
    risk_based_controls = PermissibleValue(
        text="risk_based_controls",
        title="Risk-based controls")
    risk_mapping_and_measurement = PermissibleValue(
        text="risk_mapping_and_measurement",
        title="Risk mapping and measurement")
    science_backed_tevv_practices = PermissibleValue(
        text="science_backed_tevv_practices",
        title="Science-backed TEVV practices")
    secure_software_development_practices = PermissibleValue(
        text="secure_software_development_practices",
        title="Secure software development practices")
    stakeholder_engagement = PermissibleValue(
        text="stakeholder_engagement",
        title="Stakeholder engagement")
    synthetic_content_detection_and_labeling_tools_and_techniques = PermissibleValue(
        text="synthetic_content_detection_and_labeling_tools_and_techniques",
        title="Synthetic content detection and labeling tools and techniques")
    whistleblower_protections = PermissibleValue(
        text="whistleblower_protections",
        title="Whistleblower protections")
    workforce_diversity_and_interdisciplinary_teams = PermissibleValue(
        text="workforce_diversity_and_interdisciplinary_teams",
        title="Workforce diversity and interdisciplinary teams")

    _defn = EnumDefinition(
        name="GaiGovernancePlan",
        description="The plans and actions that section A.1.2 says apply to GAI from other AI governance.",
    )

class GaiThirdPartyControl(EnumDefinitionImpl):
    """
    The existing controls that section A.1.3 says can apply to third-party GAI.
    """
    acquisition_and_procurement_due_diligence = PermissibleValue(
        text="acquisition_and_procurement_due_diligence",
        title="Acquisition and procurement due diligence",
        description="Checking a provider before acquiring its GAI technology or data.")
    software_bills_of_materials = PermissibleValue(
        text="software_bills_of_materials",
        title="Requests for software bills of materials",
        description="Asking a provider what its software is made of.")
    service_level_agreements = PermissibleValue(
        text="service_level_agreements",
        title="Application of service level agreements",
        description="Holding a provider to agreed levels of service.")
    ssae_reports = PermissibleValue(
        text="ssae_reports",
        title="Statement on standards for attestation engagement reports",
        description="Asking for a provider's attestation reports.")

    _defn = EnumDefinition(
        name="GaiThirdPartyControl",
        description="The existing controls that section A.1.3 says can apply to third-party GAI.",
    )

class GaiRedTeamingType(EnumDefinitionImpl):
    """
    The types of AI red-teaming in section A.1.5.
    """
    general_public = PermissibleValue(
        text="general_public",
        title="General Public",
        description="By general users who are not necessarily AI or technical experts.")
    expert = PermissibleValue(
        text="expert",
        title="Expert",
        description="By specialists in the domain or the context of use.")
    combination = PermissibleValue(
        text="combination",
        title="Combination",
        description="By both experts and general public participants.")
    human_ai = PermissibleValue(
        text="human_ai",
        title="Human / AI",
        description="By GAI together with human teams, specialist or not.")

    _defn = EnumDefinition(
        name="GaiRedTeamingType",
        description="The types of AI red-teaming in section A.1.5.",
    )

class GaiProvenanceTechnique(EnumDefinitionImpl):
    """
    The techniques for provenance data tracking in section A.1.6.
    """
    digital_watermarking = PermissibleValue(
        text="digital_watermarking",
        title="Digital watermarking",
        description="Placing visible or hidden marks on content.")
    metadata_recording = PermissibleValue(
        text="metadata_recording",
        title="Metadata recording",
        description="Recording facts about the content, such as its creator, date and sources.")
    digital_fingerprinting = PermissibleValue(
        text="digital_fingerprinting",
        title="Digital fingerprinting",
        description="Identifying content from its own characteristics.")
    human_authentication = PermissibleValue(
        text="human_authentication",
        title="Human authentication",
        description="Having people confirm where content came from.")

    _defn = EnumDefinition(
        name="GaiProvenanceTechnique",
        description="The techniques for provenance data tracking in section A.1.6.",
    )

class GaiIncidentHarm(EnumDefinitionImpl):
    """
    The kinds of harm that section A.1.8's definition of an AI incident names.
    """
    injury_or_harm_to_health = PermissibleValue(
        text="injury_or_harm_to_health",
        title="Injury or harm to health",
        description="To a person or group, including psychological harm and harm to mental health.")
    critical_infrastructure_disruption = PermissibleValue(
        text="critical_infrastructure_disruption",
        title="Disruption of critical infrastructure",
        description="To its management and operation.")
    rights_violations = PermissibleValue(
        text="rights_violations",
        title="Violations of rights or legal obligations",
        description="""Of human rights, or of obligations under law that protects fundamental, labor and intellectual property rights.""")
    harm_to_property_communities_or_environment = PermissibleValue(
        text="harm_to_property_communities_or_environment",
        title="Harm to property, communities, or the environment",
        description="To things and groups beyond the individual.")

    _defn = EnumDefinition(
        name="GaiIncidentHarm",
        description="The kinds of harm that section A.1.8's definition of an AI incident names.",
    )

# Slots
class slots:
    pass

slots.ai_rmf_id = Slot(uri=NIST_AI_100_1.ai_rmf_id, name="ai_rmf_id", curie=NIST_AI_100_1.curie('ai_rmf_id'),
                   model_uri=NIST_AI_600_1.ai_rmf_id, domain=None, range=URIRef)

slots.ai_rmf_subcategory_id = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_id, name="ai_rmf_subcategory_id", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_id'),
                   model_uri=NIST_AI_600_1.ai_rmf_subcategory_id, domain=None, range=Union[str, AiRmfSubcategoryIdentifier])

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_600_1.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_600_1.description, domain=None, range=Optional[str])

slots.gai_action_id = Slot(uri=NIST_AI_600_1.gai_action_id, name="gai_action_id", curie=NIST_AI_600_1.curie('gai_action_id'),
                   model_uri=NIST_AI_600_1.gai_action_id, domain=None, range=Union[str, GaiActionIdentifier])

slots.gai_consideration_type = Slot(uri=NIST_AI_600_1.gai_consideration_type, name="gai_consideration_type", curie=NIST_AI_600_1.curie('gai_consideration_type'),
                   model_uri=NIST_AI_600_1.gai_consideration_type, domain=None, range=str)

slots.gai_feedback_type = Slot(uri=NIST_AI_600_1.gai_feedback_type, name="gai_feedback_type", curie=NIST_AI_600_1.curie('gai_feedback_type'),
                   model_uri=NIST_AI_600_1.gai_feedback_type, domain=None, range=str)

slots.gaiProfile__gai_risks = Slot(uri=NIST_AI_600_1.gai_risks, name="gaiProfile__gai_risks", curie=NIST_AI_600_1.curie('gai_risks'),
                   model_uri=NIST_AI_600_1.gaiProfile__gai_risks, domain=None, range=Union[Union[dict, GaiRisk], list[Union[dict, GaiRisk]]])

slots.gaiProfile__gai_subcategories = Slot(uri=NIST_AI_600_1.gai_subcategories, name="gaiProfile__gai_subcategories", curie=NIST_AI_600_1.curie('gai_subcategories'),
                   model_uri=NIST_AI_600_1.gaiProfile__gai_subcategories, domain=None, range=Union[Union[dict, GaiSubcategory], list[Union[dict, GaiSubcategory]]])

slots.gaiProfile__gai_primary_considerations = Slot(uri=NIST_AI_600_1.gai_primary_considerations, name="gaiProfile__gai_primary_considerations", curie=NIST_AI_600_1.curie('gai_primary_considerations'),
                   model_uri=NIST_AI_600_1.gaiProfile__gai_primary_considerations, domain=None, range=Optional[Union[Union[dict, GaiPrimaryConsideration], list[Union[dict, GaiPrimaryConsideration]]]])

slots.aiRmfProfile__ai_rmf_profile_kinds = Slot(uri=NIST_AI_100_1.ai_rmf_profile_kinds, name="aiRmfProfile__ai_rmf_profile_kinds", curie=NIST_AI_100_1.curie('ai_rmf_profile_kinds'),
                   model_uri=NIST_AI_600_1.aiRmfProfile__ai_rmf_profile_kinds, domain=None, range=Union[Union[str, "AiRmfProfileKind"], list[Union[str, "AiRmfProfileKind"]]])

slots.aiRmfProfile__ai_rmf_profile_setting = Slot(uri=NIST_AI_100_1.ai_rmf_profile_setting, name="aiRmfProfile__ai_rmf_profile_setting", curie=NIST_AI_100_1.curie('ai_rmf_profile_setting'),
                   model_uri=NIST_AI_600_1.aiRmfProfile__ai_rmf_profile_setting, domain=None, range=Optional[str])

slots.aiRmfProfile__ai_rmf_profile_subcategories = Slot(uri=NIST_AI_100_1.ai_rmf_profile_subcategories, name="aiRmfProfile__ai_rmf_profile_subcategories", curie=NIST_AI_100_1.curie('ai_rmf_profile_subcategories'),
                   model_uri=NIST_AI_600_1.aiRmfProfile__ai_rmf_profile_subcategories, domain=None, range=Optional[Union[Union[str, AiRmfSubcategoryIdentifier], list[Union[str, AiRmfSubcategoryIdentifier]]]])

slots.gaiRisk__gai_risk_name = Slot(uri=NIST_AI_600_1.gai_risk_name, name="gaiRisk__gai_risk_name", curie=NIST_AI_600_1.curie('gai_risk_name'),
                   model_uri=NIST_AI_600_1.gaiRisk__gai_risk_name, domain=None, range=Union[str, "GaiRiskName"])

slots.gaiRisk__gai_risk_section = Slot(uri=NIST_AI_600_1.gai_risk_section, name="gaiRisk__gai_risk_section", curie=NIST_AI_600_1.curie('gai_risk_section'),
                   model_uri=NIST_AI_600_1.gaiRisk__gai_risk_section, domain=None, range=str,
                   pattern=re.compile(r'^2\.([1-9]|1[0-2])$'))

slots.gaiRisk__gai_risk_characteristics = Slot(uri=NIST_AI_600_1.gai_risk_characteristics, name="gaiRisk__gai_risk_characteristics", curie=NIST_AI_600_1.curie('gai_risk_characteristics'),
                   model_uri=NIST_AI_600_1.gaiRisk__gai_risk_characteristics, domain=None, range=Optional[Union[Union[str, "AiRmfCharacteristicName"], list[Union[str, "AiRmfCharacteristicName"]]]])

slots.gaiRisk__gai_risk_groupings = Slot(uri=NIST_AI_600_1.gai_risk_groupings, name="gaiRisk__gai_risk_groupings", curie=NIST_AI_600_1.curie('gai_risk_groupings'),
                   model_uri=NIST_AI_600_1.gaiRisk__gai_risk_groupings, domain=None, range=Optional[Union[Union[str, "GaiRiskGrouping"], list[Union[str, "GaiRiskGrouping"]]]])

slots.gaiRisk__gai_risk_lifecycle_stages = Slot(uri=NIST_AI_600_1.gai_risk_lifecycle_stages, name="gaiRisk__gai_risk_lifecycle_stages", curie=NIST_AI_600_1.curie('gai_risk_lifecycle_stages'),
                   model_uri=NIST_AI_600_1.gaiRisk__gai_risk_lifecycle_stages, domain=None, range=Optional[Union[Union[str, "GaiLifecycleStage"], list[Union[str, "GaiLifecycleStage"]]]])

slots.gaiRisk__gai_risk_scopes = Slot(uri=NIST_AI_600_1.gai_risk_scopes, name="gaiRisk__gai_risk_scopes", curie=NIST_AI_600_1.curie('gai_risk_scopes'),
                   model_uri=NIST_AI_600_1.gaiRisk__gai_risk_scopes, domain=None, range=Optional[Union[Union[str, "GaiRiskScope"], list[Union[str, "GaiRiskScope"]]]])

slots.gaiRisk__gai_risk_sources = Slot(uri=NIST_AI_600_1.gai_risk_sources, name="gaiRisk__gai_risk_sources", curie=NIST_AI_600_1.curie('gai_risk_sources'),
                   model_uri=NIST_AI_600_1.gaiRisk__gai_risk_sources, domain=None, range=Optional[Union[Union[str, "GaiRiskSource"], list[Union[str, "GaiRiskSource"]]]])

slots.gaiRisk__gai_risk_time_scales = Slot(uri=NIST_AI_600_1.gai_risk_time_scales, name="gaiRisk__gai_risk_time_scales", curie=NIST_AI_600_1.curie('gai_risk_time_scales'),
                   model_uri=NIST_AI_600_1.gaiRisk__gai_risk_time_scales, domain=None, range=Optional[Union[Union[str, "GaiRiskTimeScale"], list[Union[str, "GaiRiskTimeScale"]]]])

slots.gaiSubcategory__gai_subcategory_actions = Slot(uri=NIST_AI_600_1.gai_subcategory_actions, name="gaiSubcategory__gai_subcategory_actions", curie=NIST_AI_600_1.curie('gai_subcategory_actions'),
                   model_uri=NIST_AI_600_1.gaiSubcategory__gai_subcategory_actions, domain=None, range=Union[Union[dict, GaiSuggestedAction], list[Union[dict, GaiSuggestedAction]]])

slots.gaiSubcategory__gai_subcategory_actor_tasks = Slot(uri=NIST_AI_600_1.gai_subcategory_actor_tasks, name="gaiSubcategory__gai_subcategory_actor_tasks", curie=NIST_AI_600_1.curie('gai_subcategory_actor_tasks'),
                   model_uri=NIST_AI_600_1.gaiSubcategory__gai_subcategory_actor_tasks, domain=None, range=Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]])

slots.gaiSuggestedAction__gai_action_risks = Slot(uri=NIST_AI_600_1.gai_action_risks, name="gaiSuggestedAction__gai_action_risks", curie=NIST_AI_600_1.curie('gai_action_risks'),
                   model_uri=NIST_AI_600_1.gaiSuggestedAction__gai_action_risks, domain=None, range=Optional[Union[Union[str, "GaiRiskName"], list[Union[str, "GaiRiskName"]]]])

slots.gaiPrimaryConsideration__gai_consideration_sections = Slot(uri=NIST_AI_600_1.gai_consideration_sections, name="gaiPrimaryConsideration__gai_consideration_sections", curie=NIST_AI_600_1.curie('gai_consideration_sections'),
                   model_uri=NIST_AI_600_1.gaiPrimaryConsideration__gai_consideration_sections, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^A\.1(\.[1-8])?$'))

slots.gaiGovernanceConsideration__gai_governance_plans = Slot(uri=NIST_AI_600_1.gai_governance_plans, name="gaiGovernanceConsideration__gai_governance_plans", curie=NIST_AI_600_1.curie('gai_governance_plans'),
                   model_uri=NIST_AI_600_1.gaiGovernanceConsideration__gai_governance_plans, domain=None, range=Optional[Union[Union[str, "GaiGovernancePlan"], list[Union[str, "GaiGovernancePlan"]]]])

slots.gaiGovernanceConsideration__gai_third_party_controls = Slot(uri=NIST_AI_600_1.gai_third_party_controls, name="gaiGovernanceConsideration__gai_third_party_controls", curie=NIST_AI_600_1.curie('gai_third_party_controls'),
                   model_uri=NIST_AI_600_1.gaiGovernanceConsideration__gai_third_party_controls, domain=None, range=Optional[Union[Union[str, "GaiThirdPartyControl"], list[Union[str, "GaiThirdPartyControl"]]]])

slots.gaiPreDeploymentTestingConsideration__gai_structured_feedback = Slot(uri=NIST_AI_600_1.gai_structured_feedback, name="gaiPreDeploymentTestingConsideration__gai_structured_feedback", curie=NIST_AI_600_1.curie('gai_structured_feedback'),
                   model_uri=NIST_AI_600_1.gaiPreDeploymentTestingConsideration__gai_structured_feedback, domain=None, range=Optional[Union[Union[dict, GaiStructuredFeedback], list[Union[dict, GaiStructuredFeedback]]]])

slots.gaiContentProvenanceConsideration__gai_provenance_techniques = Slot(uri=NIST_AI_600_1.gai_provenance_techniques, name="gaiContentProvenanceConsideration__gai_provenance_techniques", curie=NIST_AI_600_1.curie('gai_provenance_techniques'),
                   model_uri=NIST_AI_600_1.gaiContentProvenanceConsideration__gai_provenance_techniques, domain=None, range=Optional[Union[Union[str, "GaiProvenanceTechnique"], list[Union[str, "GaiProvenanceTechnique"]]]])

slots.gaiIncidentDisclosureConsideration__gai_incident_harms = Slot(uri=NIST_AI_600_1.gai_incident_harms, name="gaiIncidentDisclosureConsideration__gai_incident_harms", curie=NIST_AI_600_1.curie('gai_incident_harms'),
                   model_uri=NIST_AI_600_1.gaiIncidentDisclosureConsideration__gai_incident_harms, domain=None, range=Optional[Union[Union[str, "GaiIncidentHarm"], list[Union[str, "GaiIncidentHarm"]]]])

slots.gaiAiRedTeaming__gai_red_teaming_types = Slot(uri=NIST_AI_600_1.gai_red_teaming_types, name="gaiAiRedTeaming__gai_red_teaming_types", curie=NIST_AI_600_1.curie('gai_red_teaming_types'),
                   model_uri=NIST_AI_600_1.gaiAiRedTeaming__gai_red_teaming_types, domain=None, range=Optional[Union[Union[str, "GaiRedTeamingType"], list[Union[str, "GaiRedTeamingType"]]]])

slots.GaiRisk_description = Slot(uri=SCHEMA.description, name="GaiRisk_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_600_1.GaiRisk_description, domain=GaiRisk, range=Optional[str])

slots.GaiSubcategory_description = Slot(uri=SCHEMA.description, name="GaiSubcategory_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_600_1.GaiSubcategory_description, domain=GaiSubcategory, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.GaiSuggestedAction_description = Slot(uri=SCHEMA.description, name="GaiSuggestedAction_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_600_1.GaiSuggestedAction_description, domain=GaiSuggestedAction, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.GaiPrimaryConsideration_title = Slot(uri=SCHEMA.name, name="GaiPrimaryConsideration_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_600_1.GaiPrimaryConsideration_title, domain=GaiPrimaryConsideration, range=str)

slots.GaiStructuredFeedback_title = Slot(uri=SCHEMA.name, name="GaiStructuredFeedback_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_600_1.GaiStructuredFeedback_title, domain=GaiStructuredFeedback, range=str)
