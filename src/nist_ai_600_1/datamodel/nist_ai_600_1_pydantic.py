from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "1.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'publication_approved': {'tag': 'publication_approved',
                                              'value': '2024-07-25'},
                     'publication_date': {'tag': 'publication_date',
                                          'value': '2024-07'}},
     'comments': ['The publication has no version number of its own, so the '
                  'version is the 1.0.0 of the AI RMF it profiles, and source is '
                  "the publication's digital object identifier. The release tags "
                  "are the schema's own versions, and "
                  'scripts/check_upstream_release.py reports when NIST changes the '
                  'file.',
                  'It imports the base and profiles modules of '
                  'lmodel/nist-ai-100-1, vendored under nist_ai_100_1/, so it '
                  'needs no network. tests/test_schema_rules.py holds them to '
                  'their hashes.',
                  'The publication is a work of the United States Government. '
                  "NOTICE says what it allows. The schema's descriptions are this "
                  "project's own words; NIST's text is in "
                  'src/nist_ai_600_1/data/.'],
     'default_prefix': 'nist_ai_600_1',
     'default_range': 'string',
     'description': 'A LinkML model of NIST AI 600-1, the Generative Artificial '
                    'Intelligence Profile of the AI Risk Management Framework: its '
                    '12 risks, the suggested actions its tables list under AI RMF '
                    'subcategories, and its four primary considerations.',
     'id': 'https://w3id.org/lmodel/nist-ai-600-1',
     'imports': ['linkml:types',
                 './nist_ai_100_1/nist_ai_100_1_base',
                 './nist_ai_100_1/nist_ai_100_1_profiles',
                 './nist_ai_600_1_risks',
                 './nist_ai_600_1_actions',
                 './nist_ai_600_1_considerations'],
     'license': 'Apache-2.0',
     'name': 'nist_ai_600_1',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_ai_100_1': {'prefix_prefix': 'nist_ai_100_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-100-1/'},
                  'nist_ai_600_1': {'prefix_prefix': 'nist_ai_600_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-600-1/'}},
     'see_also': ['https://lmodel.github.io/nist-ai-600-1',
                  'https://airc.nist.gov/Home',
                  'https://doi.org/10.6028/NIST.AI.100-1'],
     'source': 'https://doi.org/10.6028/NIST.AI.600-1',
     'source_file': 'src/nist_ai_600_1/schema/nist_ai_600_1.yaml',
     'title': 'NIST AI RMF Generative AI Profile (NIST AI 600-1)'} )

class AiRmfCharacteristicName(str, Enum):
    """
    The seven characteristics of trustworthy AI systems in section 3 of the publication.
    """
    Valid_and_Reliable = "valid_and_reliable"
    """
    Shown by evidence to meet the needs of its intended use, and works without failure over time. Figure 4 makes it a necessary condition for the others.
    """
    Safe = "safe"
    """
    Keeps people, property and the environment out of danger under defined conditions.
    """
    Secure_and_Resilient = "secure_and_resilient"
    """
    Withstands adverse events and recovers from them, and keeps confidentiality, integrity and availability through protections against attack.
    """
    Accountable_and_Transparent = "accountable_and_transparent"
    """
    Answerable for outcomes, which rests on people being able to get information about the system and its outputs. Figure 4 shows it relating to all the others.
    """
    Explainable_and_Interpretable = "explainable_and_interpretable"
    """
    Its working can be represented (how a decision was made) and its output understood in context (why, and what it means for the user).
    """
    Privacy_Enhanced = "privacy_enhanced"
    """
    Guided by the norms and practices that protect human autonomy, identity and dignity, such as anonymity, confidentiality and control.
    """
    Fair_EN_DASH_with_Harmful_Bias_Managed = "fair_with_harmful_bias_managed"
    """
    Addresses equality and equity, including harmful bias and discrimination, knowing that views of fairness differ across cultures and applications.
    """


class AiRmfActorTaskName(str, Enum):
    """
    The ten AI actor tasks and five additional AI actors of Appendix A.
    """
    AI_Design = "ai_design"
    """
    Setting what the system is for, planning and designing it, and gathering and preparing its data.
    """
    AI_Development = "ai_development"
    """
    Providing the initial infrastructure, and creating, selecting, calibrating, training and testing models.
    """
    AI_Deployment = "ai_deployment"
    """
    Deciding how the system is used and putting it into production, including pilots and compliance checks.
    """
    Operation_and_Monitoring = "operation_and_monitoring"
    """
    Running the system and regularly assessing its output and impacts.
    """
    Test_Evaluation_Verification_and_Validation_LEFT_PARENTHESISTEVVRIGHT_PARENTHESIS = "tevv"
    """
    Examining the system or its components and finding and fixing problems, throughout the lifecycle.
    """
    Human_Factors = "human_factors"
    """
    Human-centered design and evaluation, involving end users and bringing context-specific norms and values into design.
    """
    Domain_Expert = "domain_expert"
    """
    Giving knowledge of the sector or setting where the system is used.
    """
    AI_Impact_Assessment = "ai_impact_assessment"
    """
    Assessing accountability, harmful bias, impacts, product safety, liability and security.
    """
    Procurement = "procurement"
    """
    Buying AI from another party, under financial, legal or policy authority.
    """
    Governance_and_Oversight = "governance_and_oversight"
    """
    Holding management, fiduciary and legal authority for the organization where the system is designed, developed or deployed.
    """
    Third_party_entities = "third_party_entities"
    """
    Outside organizations that supply or evaluate the data, models, systems or services an organization acquires.
    """
    End_users = "end_users"
    """
    The people or groups who use the system, whether new to technology or expert in AI.
    """
    Affected_individualsSOLIDUScommunities = "affected_individuals_and_communities"
    """
    Those directly or indirectly affected by the system or its output, whether or not they interact with it.
    """
    Other_AI_actors = "other_ai_actors"
    """
    Those who set norms or guidance on AI risk, such as standards bodies, advocacy groups and researchers.
    """
    General_public = "general_public"
    """
    Those most likely to experience the impacts directly, who may motivate what other AI actors do.
    """


class AiRmfProfileKind(str, Enum):
    """
    The kinds of AI RMF profile that section 6 names.
    """
    Use_case_profile = "use_case"
    """
    The Core implemented for a specific setting or application.
    """
    Current_Profile = "current"
    """
    A temporal profile saying how AI is managed today and the related risks, in terms of current outcomes.
    """
    Target_Profile = "target"
    """
    A temporal profile saying which outcomes the desired risk management goals need.
    """
    Cross_sectoral_profile = "cross_sectoral"
    """
    Covers risks of models or applications used across use cases or sectors, or activities common to them, such as using large language models.
    """


class GaiRiskName(str, Enum):
    """
    The 12 risks of section 2.
    """
    CBRN_Information_or_Capabilities = "cbrn_information_or_capabilities"
    """
    Easier access to dangerous information or design abilities for chemical, biological, radiological or nuclear weapons.
    """
    Confabulation = "confabulation"
    """
    Confident but wrong output that can mislead users.
    """
    Dangerous_Violent_or_Hateful_Content = "dangerous_violent_or_hateful_content"
    """
    Easier production of content that incites or threatens, recommends harm, or disparages.
    """
    Data_Privacy = "data_privacy"
    """
    Leaks, misuse or de-anonymization of personal or sensitive data.
    """
    Environmental_Impacts = "environmental_impacts"
    """
    Effects on ecosystems from the heavy computing that training and operating models need.
    """
    Harmful_Bias_or_Homogenization = "harmful_bias_or_homogenization"
    """
    Worse systemic bias, unequal performance across groups or languages, and output skewed by sameness.
    """
    Human_AI_Configuration = "human_ai_configuration"
    """
    Interaction that leads people to over-rely on, anthropomorphize or become entangled with a system, or to distrust it.
    """
    Information_Integrity = "information_integrity"
    """
    Easier creation and spread of content that blurs fact and opinion, or that can drive large disinformation campaigns.
    """
    Information_Security = "information_security"
    """
    Easier offensive cyber activity, and a larger attack surface on a system, its data, code or weights.
    """
    Intellectual_Property = "intellectual_property"
    """
    Easier unauthorized copying of protected content, exposure of trade secrets, and plagiarism.
    """
    Obscene_Degrading_andSOLIDUSor_Abusive_Content = "obscene_degrading_or_abusive_content"
    """
    Easier production of harmful imagery, including synthetic abuse material and intimate images without consent.
    """
    Value_Chain_and_Component_Integration = "value_chain_and_component_integration"
    """
    Opaque use of third-party components and data, and poor supplier vetting, that weaken accountability downstream.
    """


class GaiRiskGrouping(str, Enum):
    """
    The three groups into which footnote 5 says an organization could sort the risks, as one possible way.
    """
    Technical_SOLIDUS_Model_risks = "technical_or_model"
    """
    Risks from malfunction.
    """
    Misuse_by_humans = "misuse_by_humans"
    """
    Risks from malicious use.
    """
    Ecosystem_SOLIDUS_societal_risks = "ecosystem_or_societal"
    """
    Systemic risks.
    """


class GaiLifecycleStage(str, Enum):
    """
    The lifecycle stages section 2 names for GAI. They differ from the seven stages of the AI RMF's Figure 3.
    """
    Design = "design"
    """
    Setting out the system before it is built.
    """
    Development = "development"
    """
    Building and training it.
    """
    Deployment = "deployment"
    """
    Putting it into use.
    """
    Operation = "operation"
    """
    Running it.
    """
    Decommissioning = "decommissioning"
    """
    Retiring it.
    """


class GaiRiskScope(str, Enum):
    """
    The levels where section 2 says a risk may exist.
    """
    Model_or_system = "model_or_system"
    """
    The level of one model or system.
    """
    Application_or_implementation = "application_or_implementation"
    """
    The level of one specific use case.
    """
    Ecosystem = "ecosystem"
    """
    Beyond one system or organization, such as algorithmic monocultures or effects on labor markets.
    """


class GaiRiskSource(str, Enum):
    """
    Where section 2 says a risk may come from.
    """
    Design = "design"
    """
    The design of the model itself.
    """
    Training = "training"
    """
    The training of the model.
    """
    Operation = "operation"
    """
    The operation of the model.
    """
    Inputs = "inputs"
    """
    What goes into the model or system.
    """
    Outputs = "outputs"
    """
    What the system produces.
    """
    Human_behavior = "human_behavior"
    """
    Abuse, misuse or unsafe repurposing by people, whether adversarial or not.
    """
    Human_AI_interaction = "human_ai_interaction"
    """
    How a person and a system act on each other.
    """


class GaiRiskTimeScale(str, Enum):
    """
    How section 2 says a risk may materialize over time.
    """
    Abruptly = "abrupt"
    """
    All at once, such as immediate emotional harm from a harmful deepfake image.
    """
    Across_extended_periods = "extended"
    """
    Slowly, such as the long-term effect of disinformation on trust in institutions.
    """


class GaiGovernancePlan(str, Enum):
    """
    The plans and actions that section A.1.2 says apply to GAI from other AI governance.
    """
    Accessibility_and_reasonable_accommodations = "accessibility_and_reasonable_accommodations"
    AI_actor_credentials_and_qualifications = "ai_actor_credentials_and_qualifications"
    Alignment_to_organizational_values = "alignment_to_organizational_values"
    Auditing_and_assessment = "auditing_and_assessment"
    Change_management_controls = "change_management_controls"
    Commercial_use = "commercial_use"
    Data_provenance = "data_provenance"
    Data_protection = "data_protection"
    Data_retention = "data_retention"
    Consistency_in_use_of_defining_key_terms = "consistency_in_use_of_defining_key_terms"
    Decommissioning = "decommissioning"
    Discouraging_anonymous_use = "discouraging_anonymous_use"
    Education = "education"
    Impact_assessments = "impact_assessments"
    Incident_response = "incident_response"
    Monitoring = "monitoring"
    Opt_outs = "opt_outs"
    Risk_based_controls = "risk_based_controls"
    Risk_mapping_and_measurement = "risk_mapping_and_measurement"
    Science_backed_TEVV_practices = "science_backed_tevv_practices"
    Secure_software_development_practices = "secure_software_development_practices"
    Stakeholder_engagement = "stakeholder_engagement"
    Synthetic_content_detection_and_labeling_tools_and_techniques = "synthetic_content_detection_and_labeling_tools_and_techniques"
    Whistleblower_protections = "whistleblower_protections"
    Workforce_diversity_and_interdisciplinary_teams = "workforce_diversity_and_interdisciplinary_teams"


class GaiThirdPartyControl(str, Enum):
    """
    The existing controls that section A.1.3 says can apply to third-party GAI.
    """
    Acquisition_and_procurement_due_diligence = "acquisition_and_procurement_due_diligence"
    """
    Checking a provider before acquiring its GAI technology or data.
    """
    Requests_for_software_bills_of_materials = "software_bills_of_materials"
    """
    Asking a provider what its software is made of.
    """
    Application_of_service_level_agreements = "service_level_agreements"
    """
    Holding a provider to agreed levels of service.
    """
    Statement_on_standards_for_attestation_engagement_reports = "ssae_reports"
    """
    Asking for a provider's attestation reports.
    """


class GaiRedTeamingType(str, Enum):
    """
    The types of AI red-teaming in section A.1.5.
    """
    General_Public = "general_public"
    """
    By general users who are not necessarily AI or technical experts.
    """
    Expert = "expert"
    """
    By specialists in the domain or the context of use.
    """
    Combination = "combination"
    """
    By both experts and general public participants.
    """
    Human_SOLIDUS_AI = "human_ai"
    """
    By GAI together with human teams, specialist or not.
    """


class GaiProvenanceTechnique(str, Enum):
    """
    The techniques for provenance data tracking in section A.1.6.
    """
    Digital_watermarking = "digital_watermarking"
    """
    Placing overt or covert marks on content.
    """
    Metadata_recording = "metadata_recording"
    """
    Recording facts about the content, such as its creator, date and sources.
    """
    Digital_fingerprinting = "digital_fingerprinting"
    """
    Identifying content from its own characteristics.
    """
    Human_authentication = "human_authentication"
    """
    Having people confirm where content came from.
    """


class GaiIncidentHarm(str, Enum):
    """
    The kinds of harm that section A.1.8's definition of an AI incident names.
    """
    Injury_or_harm_to_health = "injury_or_harm_to_health"
    """
    To a person or group, including psychological harm and harm to mental health.
    """
    Disruption_of_critical_infrastructure = "critical_infrastructure_disruption"
    """
    To its management and operation.
    """
    Violations_of_rights_or_legal_obligations = "rights_violations"
    """
    Of human rights, or of obligations under law that protects fundamental, labor and intellectual property rights.
    """
    Harm_to_property_communities_or_the_environment = "harm_to_property_communities_or_environment"
    """
    To things and groups beyond the individual.
    """



class AiRmfRecord(ConfiguredBaseModel):
    """
    The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct from what the publication itself lists.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nist_ai_100_1:Record',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_base'})

    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfProfile(AiRmfRecord):
    """
    An implementation of the Core's functions, categories and subcategories for a setting, application or technology, based on the adopter's requirements, risk tolerance and resources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:Profile',
         'comments': ['The publication prescribes no profile template, so only the '
                      'kinds and the subcategories are structured.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_profiles',
         'related_mappings': ['oscal:Profile']})

    ai_rmf_profile_kinds: list[AiRmfProfileKind] = Field(default=..., description="""Which of the publication's kinds of profile this is. A current profile for one use case is both.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_profile_setting: Optional[str] = Field(default=None, description="""The sector, industry, technology, organization or end use the profile covers, such as hiring.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_profile_subcategories: Optional[list[str]] = Field(default=None, description="""The subcategories the profile selects. An adopter may select from them rather than apply all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class GaiRisk(ConfiguredBaseModel):
    """
    A risk that section 2 defines as unique to or made worse by the development and use of GAI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:Risk',
         'comments': ['The publication gives a risk its section, its definition, its '
                      'trustworthiness characteristics and, in a footnote, its '
                      'groupings. It assigns no lifecycle stage, scope, source or time '
                      'scale to a risk, since those depend on the model, system or use '
                      'case. An adopter fills them in.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_risks',
         'related_mappings': ['nist_ai_100_1:Risk'],
         'slot_usage': {'description': {'description': "The risk's definition in "
                                                       'section 2.',
                                        'name': 'description'}}})

    description: Optional[str] = Field(default=None, description="""The risk's definition in section 2.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_risk_name: GaiRiskName = Field(default=..., description="""Which of the 12 risks this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_section: str = Field(default=..., description="""The subsection of section 2 that discusses the risk, such as 2.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_characteristics: Optional[list[AiRmfCharacteristicName]] = Field(default=None, description="""The AI RMF's trustworthiness characteristics that the subsection names for the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_groupings: Optional[list[GaiRiskGrouping]] = Field(default=None, description="""The groups footnote 5 suggests for the risk. The footnote lists Data Privacy under all three.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_lifecycle_stages: Optional[list[GaiLifecycleStage]] = Field(default=None, description="""The lifecycle stages where the risk can arise for the adopter's model, system or use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_scopes: Optional[list[GaiRiskScope]] = Field(default=None, description="""The levels where the risk exists for the adopter's model, system or use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_sources: Optional[list[GaiRiskSource]] = Field(default=None, description="""Where the risk comes from for the adopter's model, system or use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_time_scales: Optional[list[GaiRiskTimeScale]] = Field(default=None, description="""How the risk materializes over time for the adopter's model, system or use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })

    @field_validator('gai_risk_section')
    def pattern_gai_risk_section(cls, v):
        pattern=re.compile(r"^2\.([1-9]|1[0-2])$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_risk_section format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_risk_section format: {v}"
            raise ValueError(err_msg)
        return v


class GaiSubcategory(ConfiguredBaseModel):
    """
    An AI RMF subcategory as one table of section 3 addresses it. The Profile covers only some of the 72.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:Subcategory',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_actions',
         'slot_usage': {'description': {'description': "The subcategory's statement as "
                                                       'the table restates it.',
                                        'name': 'description',
                                        'pattern': '^\\s*\\S',
                                        'required': True}}})

    ai_rmf_subcategory_id: str = Field(default=..., description="""The subcategory's identifier, such as GOVERN 1.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiSubcategory']} })
    description: str = Field(default=..., description="""The subcategory's statement as the table restates it.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_subcategory_actions: list[GaiSuggestedAction] = Field(default=..., description="""The suggested actions the table lists.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['GaiSubcategory']} })
    gai_subcategory_actor_tasks: Optional[list[AiRmfActorTaskName]] = Field(default=None, description="""The AI actor tasks the table names. They belong to the table and not to one action: the publication says not every task applies to every action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiSubcategory']} })

    @field_validator('description')
    def pattern_description(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid description format: {v}"
            raise ValueError(err_msg)
        return v


class GaiSuggestedAction(ConfiguredBaseModel):
    """
    A step an organization or AI actor can take to manage GAI risks, which one row of a table states.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_ai_600_1:SuggestedAction',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_actions',
         'related_mappings': ['stix:StixCourseOfAction'],
         'slot_usage': {'description': {'description': "The action's text in the "
                                                       'table.',
                                        'name': 'description',
                                        'pattern': '^\\s*\\S',
                                        'required': True}}})

    gai_action_id: str = Field(default=..., description="""The action's identifier, such as GV-1.1-001.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiSuggestedAction']} })
    description: str = Field(default=..., description="""The action's text in the table.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_action_risks: Optional[list[GaiRiskName]] = Field(default=None, description="""The GAI risks the row tags the action with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiSuggestedAction']} })

    @field_validator('description')
    def pattern_description(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid description format: {v}"
            raise ValueError(err_msg)
        return v


class GaiPrimaryConsideration(ConfiguredBaseModel):
    """
    One of the four primary considerations of Appendix A, which also inform the suggested actions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nist_ai_600_1:PrimaryConsideration',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations',
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    gai_consideration_type: Literal["GaiPrimaryConsideration"] = Field(default="GaiPrimaryConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiGovernanceConsideration(GaiPrimaryConsideration):
    """
    How an organization's governance can be revisited for GAI, including across the AI value chain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:GovernanceConsideration',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_governance_plans: Optional[list[GaiGovernancePlan]] = Field(default=None, description="""The plans and actions that section A.1.2 lists from other AI governance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiGovernanceConsideration']} })
    gai_third_party_controls: Optional[list[GaiThirdPartyControl]] = Field(default=None, description="""The existing controls that section A.1.3 says can apply to third-party GAI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiGovernanceConsideration']} })
    gai_consideration_type: Literal["GaiGovernanceConsideration"] = Field(default="GaiGovernanceConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiPreDeploymentTestingConsideration(GaiPrimaryConsideration):
    """
    How GAI can be tested before deployment while better approaches mature, and where current tests fall short.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:PreDeploymentTestingConsideration',
         'comments': ['Section A.1.7 calls the feedback approaches of section A.1.5 '
                      'part of this consideration.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_structured_feedback: Optional[list[Union[GaiParticipatoryEngagement,GaiFieldTesting,GaiAiRedTeaming]]] = Field(default=None, description="""The kinds of structured public feedback section A.1.5 gives as examples.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPreDeploymentTestingConsideration']} })
    gai_consideration_type: Literal["GaiPreDeploymentTestingConsideration"] = Field(default="GaiPreDeploymentTestingConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiContentProvenanceConsideration(GaiPrimaryConsideration):
    """
    How tracking the origin and history of content helps tell authentic content from synthetic content.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:ContentProvenanceConsideration',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_provenance_techniques: Optional[list[GaiProvenanceTechnique]] = Field(default=None, description="""The well-known techniques for provenance data tracking that section A.1.6 names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiContentProvenanceConsideration']} })
    gai_consideration_type: Literal["GaiContentProvenanceConsideration"] = Field(default="GaiContentProvenanceConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiIncidentDisclosureConsideration(GaiPrimaryConsideration):
    """
    How documenting, reporting and sharing AI incidents helps prevent harm, though no formal channels exist.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:IncidentDisclosureConsideration',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_incident_harms: Optional[list[GaiIncidentHarm]] = Field(default=None, description="""The kinds of harm that section A.1.8's definition of an AI incident names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiIncidentDisclosureConsideration']} })
    gai_consideration_type: Literal["GaiIncidentDisclosureConsideration"] = Field(default="GaiIncidentDisclosureConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiStructuredFeedback(ConfiguredBaseModel):
    """
    A way of using structured public feedback to evaluate whether GAI systems perform as intended.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nist_ai_600_1:StructuredFeedback',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations',
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    gai_feedback_type: Literal["GaiStructuredFeedback"] = Field(default="GaiStructuredFeedback", description="""Which of the three classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiStructuredFeedback']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class GaiParticipatoryEngagement(GaiStructuredFeedback):
    """
    Asking civil society groups, affected communities and users for feedback, such as through focus groups or surveys.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:ParticipatoryEngagement',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_feedback_type: Literal["GaiParticipatoryEngagement"] = Field(default="GaiParticipatoryEngagement", description="""Which of the three classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiStructuredFeedback']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class GaiFieldTesting(GaiStructuredFeedback):
    """
    Structured settings that show how people interact with and use AI-generated information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:FieldTesting',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_feedback_type: Literal["GaiFieldTesting"] = Field(default="GaiFieldTesting", description="""Which of the three classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiStructuredFeedback']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class GaiAiRedTeaming(GaiStructuredFeedback):
    """
    A structured exercise that probes an AI system for flaws and vulnerabilities, often with its developers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:AiRedTeaming',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_red_teaming_types: Optional[list[GaiRedTeamingType]] = Field(default=None, description="""The kinds of AI red-teaming that may suit the use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiAiRedTeaming']} })
    gai_feedback_type: Literal["GaiAiRedTeaming"] = Field(default="GaiAiRedTeaming", description="""Which of the three classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiStructuredFeedback']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class GaiProfile(AiRmfProfile):
    """
    The Generative AI Profile as a whole, a cross-sectoral profile of the AI RMF and a companion resource to it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:Profile',
         'comments': ['It holds actions for only some subcategories, and the '
                      'publication says more may be added later.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
         'tree_root': True})

    gai_risks: list[GaiRisk] = Field(default=..., description="""The 12 risks of section 2.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile']} })
    gai_subcategories: list[GaiSubcategory] = Field(default=..., description="""The tables of section 3, in the publication's order.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile']} })
    gai_primary_considerations: Optional[list[Union[GaiGovernanceConsideration,GaiPreDeploymentTestingConsideration,GaiContentProvenanceConsideration,GaiIncidentDisclosureConsideration]]] = Field(default=None, description="""The four primary considerations of Appendix A.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile']} })
    ai_rmf_profile_kinds: list[AiRmfProfileKind] = Field(default=..., description="""Which of the publication's kinds of profile this is. A current profile for one use case is both.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_profile_setting: Optional[str] = Field(default=None, description="""The sector, industry, technology, organization or end use the profile covers, such as hiring.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_profile_subcategories: Optional[list[str]] = Field(default=None, description="""The subcategories the profile selects. An adopter may select from them rather than apply all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AiRmfRecord.model_rebuild()
AiRmfProfile.model_rebuild()
GaiRisk.model_rebuild()
GaiSubcategory.model_rebuild()
GaiSuggestedAction.model_rebuild()
GaiPrimaryConsideration.model_rebuild()
GaiGovernanceConsideration.model_rebuild()
GaiPreDeploymentTestingConsideration.model_rebuild()
GaiContentProvenanceConsideration.model_rebuild()
GaiIncidentDisclosureConsideration.model_rebuild()
GaiStructuredFeedback.model_rebuild()
GaiParticipatoryEngagement.model_rebuild()
GaiFieldTesting.model_rebuild()
GaiAiRedTeaming.model_rebuild()
GaiProfile.model_rebuild()
