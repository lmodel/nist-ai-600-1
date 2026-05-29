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


metamodel_version = "1.11.0"
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


linkml_meta = LinkMLMeta({'default_prefix': 'nist_ai_600_1',
     'default_range': 'string',
     'description': 'LinkML schema for NIST AI 600-1, the Generative Artificial '
                    'Intelligence\n'
                    'Profile of the AI Risk Management Framework (July 2024).\n'
                    '\n'
                    'This is a **cross-sectoral profile** and a *companion '
                    'resource* to\n'
                    'NIST AI 100-1 (AI RMF 1.0). It defines risks that are novel '
                    'to or\n'
                    'exacerbated by the use of Generative AI (GAI) and provides a '
                    'set of\n'
                    'suggested actions, organised by AI RMF subcategory, that\n'
                    'organisations can take to govern, map, measure, and manage '
                    'those\n'
                    'risks.\n'
                    '\n'
                    'This schema is **standalone** - it inlines the minimal AI '
                    'RMF\n'
                    'base scaffolding (`NamedThing`, lifecycle / trustworthiness '
                    '/\n'
                    'actor-task enums, `SubcategoryCode` type) needed to express '
                    'the\n'
                    'GAI Profile so it has no schema-level dependency on the '
                    'sibling\n'
                    '`nist-ai-rmf` schema. Cross-references to AI RMF 1.0 '
                    'elements\n'
                    'are recorded as `*_mappings` for traceability.\n'
                    '\n'
                    'The schema covers:\n'
                    '  * 12 GAI risk categories (Section 2)\n'
                    '  * Risk dimensions (lifecycle stage, scope, source, time '
                    'scale)\n'
                    '  * `SuggestedAction` entries (Section 3 tables) linked to AI '
                    'RMF\n'
                    '    subcategories\n'
                    '  * Primary GAI Considerations (Appendix A): Governance,\n'
                    '    Pre-Deployment Testing, Content Provenance, Incident '
                    'Disclosure\n'
                    '  * Structured Public Feedback methods and AI Red-teaming '
                    'types',
     'id': 'https://w3id.org/lmodel/nist-ai-600-1',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'nist-ai-600-1',
     'prefixes': {'dcterms': {'prefix_prefix': 'dcterms',
                              'prefix_reference': 'http://purl.org/dc/terms/'},
                  'doi': {'prefix_prefix': 'doi',
                          'prefix_reference': 'https://doi.org/'},
                  'gist_linkml': {'prefix_prefix': 'gist_linkml',
                                  'prefix_reference': 'https://w3id.org/lmodel/gist/'},
                  'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'iso29100': {'prefix_prefix': 'iso29100',
                               'prefix_reference': 'https://w3id.org/lmodel/iso29100/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_ai_100_1': {'prefix_prefix': 'nist_ai_100_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-100-1/'},
                  'nist_ai_600_1': {'prefix_prefix': 'nist_ai_600_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-600-1/'},
                  'nist_csf': {'prefix_prefix': 'nist_csf',
                               'prefix_reference': 'https://w3id.org/lmodel/nist-csf-v2/'},
                  'oscal_catalog': {'prefix_prefix': 'oscal_catalog',
                                    'prefix_reference': 'https://w3id.org/lmodel/oscal_catalog/'},
                  'oscal_profile': {'prefix_prefix': 'oscal_profile',
                                    'prefix_reference': 'https://w3id.org/lmodel/oscal_profile/'},
                  'rdf': {'prefix_prefix': 'rdf',
                          'prefix_reference': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'},
                  'rdfs': {'prefix_prefix': 'rdfs',
                           'prefix_reference': 'http://www.w3.org/2000/01/rdf-schema#'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'skos': {'prefix_prefix': 'skos',
                           'prefix_reference': 'http://www.w3.org/2004/02/skos/core#'},
                  'stix': {'prefix_prefix': 'stix',
                           'prefix_reference': 'https://w3id.org/lmodel/stix/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://doi.org/10.6028/NIST.AI.600-1',
                  'https://airc.nist.gov/Home',
                  'https://doi.org/10.6028/NIST.AI.100-1'],
     'source': 'https://doi.org/10.6028/NIST.AI.600-1',
     'source_file': 'src/nist_ai_600_1/schema/nist_ai_600_1.yaml',
     'subsets': {'gai_actions': {'description': 'Suggested Actions organised by AI '
                                                'RMF subcategory (Section 3).',
                                 'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
                                 'name': 'gai_actions'},
                 'gai_base': {'description': 'Minimal AI RMF base scaffolding '
                                             'inlined to keep this schema\n'
                                             'standalone (abstract `NamedThing`, '
                                             'lifecycle / trustworthiness /\n'
                                             'actor-task enums, `SubcategoryCode` '
                                             'type). Conceptually mirrors\n'
                                             'the equivalents defined in NIST AI '
                                             '100-1; see `*_mappings` for\n'
                                             'cross-references.',
                              'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
                              'name': 'gai_base'},
                 'gai_considerations': {'description': 'Primary GAI Considerations '
                                                       '(Appendix A): Governance,\n'
                                                       'Pre-Deployment Testing, '
                                                       'Content Provenance, '
                                                       'Incident Disclosure.',
                                        'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
                                        'name': 'gai_considerations'},
                 'gai_core': {'description': 'Foundational GAI Profile concepts - '
                                             'the 12 risks and their\n'
                                             'dimensions (Section 2).',
                              'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
                              'name': 'gai_core'},
                 'gai_feedback': {'description': 'Structured Public Feedback '
                                                 'methods and AI Red-teaming\n'
                                                 '(Appendix A.1.5).',
                                  'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
                                  'name': 'gai_feedback'}},
     'title': 'NIST AI RMF Generative AI Profile (NIST AI 600-1)',
     'types': {'GaiActionId': {'base': 'str',
                               'description': 'Action identifier used in NIST AI '
                                              '600-1 Section 3, of the form\n'
                                              '"<prefix>-<category>.<subcategory>-<seq>" '
                                              '- e.g., "GV-1.1-001".\n'
                                              'Prefixes: GV (Govern), MP (Map), MS '
                                              '(Measure), MG (Manage).',
                               'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
                               'name': 'GaiActionId',
                               'pattern': '^(GV|MP|MS|MG)-[0-9]+\\.[0-9]+-[0-9]{3}$',
                               'typeof': 'string',
                               'uri': 'xsd:string'},
               'SubcategoryCode': {'base': 'str',
                                   'description': 'Identifier for an AI RMF Core '
                                                  'subcategory referenced by a\n'
                                                  'suggested action (e.g., "GOVERN '
                                                  '1.1"). Mirrors the\n'
                                                  '`SubcategoryCode` type defined '
                                                  'by NIST AI 100-1.',
                                   'exact_mappings': ['nist_ai_100_1:SubcategoryCode'],
                                   'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
                                   'name': 'SubcategoryCode',
                                   'pattern': '^(GOVERN|MAP|MEASURE|MANAGE) '
                                              '[0-9]+\\.[0-9]+$',
                                   'typeof': 'string',
                                   'uri': 'xsd:string'}}} )

class AiLifecycleStageEnum(str, Enum):
    """
    AI lifecycle stages enumerated in NIST AI 600-1 Section 2:
"Risks can arise during design, development, deployment,
operation, and/or decommissioning."
    """
    DESIGN = "DESIGN"
    """
    Articulating system concept, objectives, requirements.
    """
    DEVELOPMENT = "DEVELOPMENT"
    """
    Building, training, and tuning the GAI model or system.
    """
    DEPLOYMENT = "DEPLOYMENT"
    """
    Placing the GAI system into a production environment.
    """
    OPERATION = "OPERATION"
    """
    Running and monitoring the GAI system in use.
    """
    DECOMMISSIONING = "DECOMMISSIONING"
    """
    Retiring or phasing out the GAI system.
    """


class TrustworthinessCharacteristicEnum(str, Enum):
    """
    The seven characteristics of trustworthy AI from NIST AI 100-1
(AI RMF 1.0) Part 1 §3, referenced throughout NIST AI 600-1
Section 2 as "Trustworthy AI Characteristics" tags on each
GAI risk.
    """
    VALID_AND_RELIABLE = "VALID_AND_RELIABLE"
    """
    Confirmation that requirements for a specific intended use
    have been fulfilled (validation) and that the system
    performs as required without failure (reliability).
    """
    SAFE = "SAFE"
    """
    The system does not, under defined conditions, lead to a
    state in which human life, health, property, or the
    environment is endangered.
    """
    SECURE_AND_RESILIENT = "SECURE_AND_RESILIENT"
    """
    The system can withstand unexpected adverse events or
    changes (resilient) and maintain confidentiality,
    integrity, and availability (secure).
    """
    ACCOUNTABLE_AND_TRANSPARENT = "ACCOUNTABLE_AND_TRANSPARENT"
    """
    Trustworthy AI depends on accountability, which presupposes
    transparency about the system and its outputs.
    """
    EXPLAINABLE_AND_INTERPRETABLE = "EXPLAINABLE_AND_INTERPRETABLE"
    """
    Explainability concerns the mechanisms underlying an AI
    system's operation; interpretability concerns the meaning
    of its output in context.
    """
    PRIVACY_ENHANCED = "PRIVACY_ENHANCED"
    """
    Norms and practices that help safeguard human autonomy,
    identity, and dignity - including anonymity, confidentiality,
    and control over personal information.
    """
    FAIR_WITH_HARMFUL_BIAS_MANAGED = "FAIR_WITH_HARMFUL_BIAS_MANAGED"
    """
    Addressing equality and equity issues such as harmful bias
    and discrimination across cultures and applications.
    """


class AiActorTaskEnum(str, Enum):
    """
    AI Actor Tasks referenced by the Suggested Actions tables in
NIST AI 600-1 Section 3 (and defined in NIST AI 100-1
Appendix A).
    """
    GOVERNANCE_AND_OVERSIGHT = "GOVERNANCE_AND_OVERSIGHT"
    """
    Management, fiduciary, and legal authority for the organization.
    """
    AI_DESIGN = "AI_DESIGN"
    """
    Concept, objectives, planning, design, and data collection.
    """
    AI_DEVELOPMENT = "AI_DEVELOPMENT"
    """
    Model building, selection, calibration, training, and testing.
    """
    AI_DEPLOYMENT = "AI_DEPLOYMENT"
    """
    Contextual decisions on how the AI system is used and deployed.
    """
    AI_IMPACT_ASSESSMENT = "AI_IMPACT_ASSESSMENT"
    """
    Assessing accountability, bias, impacts, safety, liability, security.
    """
    OPERATION_AND_MONITORING = "OPERATION_AND_MONITORING"
    """
    Operating the AI system and assessing system output and impacts.
    """
    TEVV = "TEVV"
    """
    Test, Evaluation, Verification, and Validation tasks.
    """
    DOMAIN_EXPERTS = "DOMAIN_EXPERTS"
    """
    Multidisciplinary practitioners with sector or context expertise.
    """
    END_USERS = "END_USERS"
    """
    Individuals or groups using the AI system for specific purposes.
    """
    HUMAN_FACTORS = "HUMAN_FACTORS"
    """
    Human-centered design practices and end-user involvement.
    """
    AFFECTED_INDIVIDUALS_AND_COMMUNITIES = "AFFECTED_INDIVIDUALS_AND_COMMUNITIES"
    """
    Individuals, groups, or communities directly or indirectly affected.
    """
    PROCUREMENT = "PROCUREMENT"
    """
    Acquisition of AI models, products, or services from third parties.
    """
    THIRD_PARTY_ENTITIES = "THIRD_PARTY_ENTITIES"
    """
    Providers, developers, vendors, and evaluators external to the deploying organization.
    """


class GaiRiskCategoryEnum(str, Enum):
    """
    The 12 risks unique to or exacerbated by Generative AI as
enumerated in NIST AI 600-1 Section 2.
    """
    CBRN_INFORMATION_OR_CAPABILITIES = "CBRN_INFORMATION_OR_CAPABILITIES"
    """
    Eased access to or synthesis of materially nefarious
    information or design capabilities related to chemical,
    biological, radiological, or nuclear (CBRN) weapons or
    other dangerous materials or agents.
    """
    CONFABULATION = "CONFABULATION"
    """
    The production of confidently stated but erroneous or
    false content (colloquially "hallucinations" or
    "fabrications") by which users may be misled or deceived.
    """
    DANGEROUS_VIOLENT_OR_HATEFUL_CONTENT = "DANGEROUS_VIOLENT_OR_HATEFUL_CONTENT"
    """
    Eased production of and access to violent, inciting,
    radicalizing, or threatening content as well as
    recommendations to carry out self-harm or conduct illegal
    activities. Includes difficulty controlling public
    exposure to hateful and disparaging or stereotyping
    content.
    """
    DATA_PRIVACY = "DATA_PRIVACY"
    """
    Impacts due to leakage and unauthorized use, disclosure, or
    de-anonymization of biometric, health, location, or other
    personally identifiable information or sensitive data.
    """
    ENVIRONMENTAL_IMPACTS = "ENVIRONMENTAL_IMPACTS"
    """
    Impacts due to high compute resource utilization in
    training or operating GAI models, and related outcomes that
    may adversely impact ecosystems.
    """
    HARMFUL_BIAS_OR_HOMOGENIZATION = "HARMFUL_BIAS_OR_HOMOGENIZATION"
    """
    Amplification and exacerbation of historical, societal,
    and systemic biases; performance disparities between
    sub-groups or languages, possibly due to non-representative
    training data, resulting in discrimination, amplification
    of biases, or incorrect presumptions about performance;
    undesired homogeneity that skews system or model outputs.
    """
    HUMAN_AI_CONFIGURATION = "HUMAN_AI_CONFIGURATION"
    """
    Arrangements of or interactions between a human and an AI
    system which can result in the human inappropriately
    anthropomorphising GAI systems or experiencing algorithmic
    aversion, automation bias, over-reliance, or emotional
    entanglement with GAI systems.
    """
    INFORMATION_INTEGRITY = "INFORMATION_INTEGRITY"
    """
    Lowered barrier to entry to generate and support the
    exchange and consumption of content which may not
    distinguish fact from opinion or fiction or acknowledge
    uncertainties, or could be leveraged for large-scale
    dis- and mis-information campaigns.
    """
    INFORMATION_SECURITY = "INFORMATION_SECURITY"
    """
    Lowered barriers for offensive cyber capabilities,
    including via automated discovery and exploitation of
    vulnerabilities; increased attack surface for targeted
    cyberattacks, which may compromise a system's availability
    or the confidentiality or integrity of training data,
    code, or model weights.
    """
    INTELLECTUAL_PROPERTY = "INTELLECTUAL_PROPERTY"
    """
    Eased production or replication of alleged copyrighted,
    trademarked, or licensed content without authorization
    (possibly outside fair use); eased exposure of trade
    secrets; or plagiarism or illegal replication.
    """
    OBSCENE_DEGRADING_OR_ABUSIVE_CONTENT = "OBSCENE_DEGRADING_OR_ABUSIVE_CONTENT"
    """
    Eased production of and access to obscene, degrading,
    and/or abusive imagery which can cause harm, including
    synthetic child sexual abuse material (CSAM) and
    nonconsensual intimate images (NCII) of adults.
    """
    VALUE_CHAIN_AND_COMPONENT_INTEGRATION = "VALUE_CHAIN_AND_COMPONENT_INTEGRATION"
    """
    Non-transparent or untraceable integration of upstream
    third-party components, including data that has been
    improperly obtained or not processed and cleaned due to
    increased automation from GAI; improper supplier vetting
    across the AI lifecycle; or other issues that diminish
    transparency or accountability for downstream users.
    """


class GaiRiskCategorizationEnum(str, Enum):
    """
    Higher-level grouping of GAI risks, derived from the UK's
International Scientific Report on the Safety of Advanced AI
(NIST AI 600-1 Section 2, footnote 5).
    """
    TECHNICAL_OR_MODEL_RISKS = "TECHNICAL_OR_MODEL_RISKS"
    """
    Risks from malfunction. Examples include confabulation;
    dangerous or violent recommendations; data privacy; value
    chain and component integration; harmful bias and
    homogenization.
    """
    MISUSE_BY_HUMANS = "MISUSE_BY_HUMANS"
    """
    Risks from malicious use. Examples include CBRN information
    or capabilities; data privacy; human-AI configuration;
    obscene, degrading, and/or abusive content; information
    integrity; information security.
    """
    ECOSYSTEM_OR_SOCIETAL_RISKS = "ECOSYSTEM_OR_SOCIETAL_RISKS"
    """
    Systemic risks. Examples include data privacy;
    environmental impacts; intellectual property.
    """


class GaiRiskScopeEnum(str, Enum):
    """
    The scope at which a GAI risk may manifest (Section 2).
    """
    MODEL_OR_SYSTEM = "MODEL_OR_SYSTEM"
    """
    Individual GAI model or system level.
    """
    APPLICATION_OR_IMPLEMENTATION = "APPLICATION_OR_IMPLEMENTATION"
    """
    Specific application or implementation - i.e., a particular
    use case.
    """
    ECOSYSTEM = "ECOSYSTEM"
    """
    Beyond a single system or organizational context - e.g.,
    algorithmic monocultures, labor-market impacts, creative
    economies.
    """


class GaiRiskSourceEnum(str, Enum):
    """
    The source(s) from which a GAI risk may emerge (Section 2).
    """
    DESIGN = "DESIGN"
    """
    From decisions made during model or system design.
    """
    TRAINING = "TRAINING"
    """
    From the training data or training process.
    """
    OPERATION = "OPERATION"
    """
    From operating the GAI model or system.
    """
    MODEL_INPUTS = "MODEL_INPUTS"
    """
    From inputs supplied to the model at inference time.
    """
    MODEL_OUTPUTS = "MODEL_OUTPUTS"
    """
    From the GAI system's generated outputs.
    """
    HUMAN_BEHAVIOR = "HUMAN_BEHAVIOR"
    """
    From human behaviour - abuse, misuse, or unsafe repurposing
    by humans (adversarial or not).
    """
    HUMAN_AI_INTERACTION = "HUMAN_AI_INTERACTION"
    """
    From interactions between a human and the AI system.
    """


class GaiRiskTimeScaleEnum(str, Enum):
    """
    The time scale over which a GAI risk may materialise
(Section 2).
    """
    IMMEDIATE = "IMMEDIATE"
    """
    Materialises abruptly (e.g., distribution of deepfakes).
    """
    PROLONGED = "PROLONGED"
    """
    Materialises across extended periods (e.g., long-term
    effect of disinformation on societal trust).
    """


class GaiActionFunctionPrefixEnum(str, Enum):
    """
    Two-letter function prefix used in GAI Action IDs.
    """
    GV = "GV"
    """
    Govern function.
    """
    MP = "MP"
    """
    Map function.
    """
    MS = "MS"
    """
    Measure function.
    """
    MG = "MG"
    """
    Manage function.
    """


class PrimaryConsiderationEnum(str, Enum):
    """
    The four overarching themes derived from the GAI PWG
consultation process (Appendix A).
    """
    GOVERNANCE = "GOVERNANCE"
    """
    How organizational governance regimes may be re-evaluated
    and adjusted for GAI contexts (A.1).
    """
    PRE_DEPLOYMENT_TESTING = "PRE_DEPLOYMENT_TESTING"
    """
    Test, evaluation, validation, and verification practices
    appropriate for GAI prior to deployment (A.1.4).
    """
    CONTENT_PROVENANCE = "CONTENT_PROVENANCE"
    """
    Digital transparency mechanisms (provenance data tracking,
    watermarking, synthetic content detection) for tracing
    origin and history of content (A.1.6 - A.1.7).
    """
    INCIDENT_DISCLOSURE = "INCIDENT_DISCLOSURE"
    """
    Documenting, reporting, and sharing information about AI
    incidents to mitigate harm and improve risk management
    (A.1.8).
    """


class StructuredFeedbackMethodEnum(str, Enum):
    """
    Categories of structured public feedback for GAI risk
management (Appendix A.1.5).
    """
    PARTICIPATORY_ENGAGEMENT_METHODS = "PARTICIPATORY_ENGAGEMENT_METHODS"
    """
    Methods used to solicit feedback from civil society groups,
    affected communities, and users (focus groups, small user
    studies, surveys).
    """
    FIELD_TESTING = "FIELD_TESTING"
    """
    Methods used to determine how people interact with,
    consume, use, and make sense of AI-generated information
    (UX, usability, randomised experiments).
    """
    AI_RED_TEAMING = "AI_RED_TEAMING"
    """
    A structured testing exercise used to probe an AI system
    to find flaws and vulnerabilities such as inaccurate,
    harmful, or discriminatory outputs.
    """


class RedTeamingTypeEnum(str, Enum):
    """
    Types of AI red-teaming exercises (Appendix A.1.5).
    """
    GENERAL_PUBLIC = "GENERAL_PUBLIC"
    """
    Performed by general users not necessarily having AI or
    technical expertise.
    """
    EXPERT = "EXPERT"
    """
    Performed by specialists with expertise in the domain or
    specific red-teaming context (medicine, biotech,
    cybersecurity).
    """
    COMBINATION = "COMBINATION"
    """
    Hybrid exercises using both expert and general-public
    participants.
    """
    HUMAN_AND_AI = "HUMAN_AND_AI"
    """
    Performed by GAI in combination with specialist or
    non-specialist human teams.
    """


class ProvenanceTechniqueEnum(str, Enum):
    """
    Provenance data tracking techniques for GAI content
(Appendix A.1.6). "Some well-known techniques for provenance
data tracking include digital watermarking, metadata
recording, digital fingerprinting, and human authentication,
among others."
    """
    DIGITAL_WATERMARKING = "DIGITAL_WATERMARKING"
    """
    Overt or covert digital watermarks embedded in content to
    allow downstream verification of origin.
    """
    METADATA_RECORDING = "METADATA_RECORDING"
    """
    Recording metadata about content (creator, date/time,
    location, modifications, sources) for text, image, video,
    audio, or underlying datasets.
    """
    DIGITAL_FINGERPRINTING = "DIGITAL_FINGERPRINTING"
    """
    Computing a content-derived identifier that can be matched
    against a reference store to detect known content.
    """
    HUMAN_AUTHENTICATION = "HUMAN_AUTHENTICATION"
    """
    Human-mediated verification of content origin or
    authenticity.
    """


class GovernancePracticeEnum(str, Enum):
    """
    Governance plans and actions for GAI systems enumerated in
NIST AI 600-1 Appendix A.1.2 ("Organizational Governance").
    """
    ACCESSIBILITY_AND_REASONABLE_ACCOMMODATIONS = "ACCESSIBILITY_AND_REASONABLE_ACCOMMODATIONS"
    """
    Accessibility and reasonable accommodations.
    """
    AI_ACTOR_CREDENTIALS_AND_QUALIFICATIONS = "AI_ACTOR_CREDENTIALS_AND_QUALIFICATIONS"
    """
    AI actor credentials and qualifications.
    """
    ALIGNMENT_TO_ORGANIZATIONAL_VALUES = "ALIGNMENT_TO_ORGANIZATIONAL_VALUES"
    """
    Alignment to organizational values.
    """
    AUDITING_AND_ASSESSMENT = "AUDITING_AND_ASSESSMENT"
    """
    Auditing and assessment.
    """
    CHANGE_MANAGEMENT_CONTROLS = "CHANGE_MANAGEMENT_CONTROLS"
    """
    Change-management controls.
    """
    COMMERCIAL_USE = "COMMERCIAL_USE"
    """
    Commercial use governance.
    """
    DATA_PROVENANCE = "DATA_PROVENANCE"
    """
    Data provenance.
    """
    DATA_PROTECTION = "DATA_PROTECTION"
    """
    Data protection.
    """
    DATA_RETENTION = "DATA_RETENTION"
    """
    Data retention.
    """
    CONSISTENCY_IN_USE_OF_DEFINING_KEY_TERMS = "CONSISTENCY_IN_USE_OF_DEFINING_KEY_TERMS"
    """
    Consistency in use of defining key terms.
    """
    DECOMMISSIONING = "DECOMMISSIONING"
    """
    Decommissioning practices.
    """
    DISCOURAGING_ANONYMOUS_USE = "DISCOURAGING_ANONYMOUS_USE"
    """
    Discouraging anonymous use.
    """
    EDUCATION = "EDUCATION"
    """
    Education on GAI risks and responsible use.
    """
    IMPACT_ASSESSMENTS = "IMPACT_ASSESSMENTS"
    """
    Impact assessments.
    """
    INCIDENT_RESPONSE = "INCIDENT_RESPONSE"
    """
    Incident response procedures.
    """
    MONITORING = "MONITORING"
    """
    Ongoing monitoring of GAI systems.
    """
    OPT_OUTS = "OPT_OUTS"
    """
    User opt-out mechanisms.
    """
    RISK_BASED_CONTROLS = "RISK_BASED_CONTROLS"
    """
    Risk-based controls.
    """
    RISK_MAPPING_AND_MEASUREMENT = "RISK_MAPPING_AND_MEASUREMENT"
    """
    Risk mapping and measurement.
    """
    SCIENCE_BACKED_TEVV_PRACTICES = "SCIENCE_BACKED_TEVV_PRACTICES"
    """
    Science-backed test, evaluation, validation, and verification practices.
    """
    SECURE_SOFTWARE_DEVELOPMENT_PRACTICES = "SECURE_SOFTWARE_DEVELOPMENT_PRACTICES"
    """
    Secure software development practices.
    """
    STAKEHOLDER_ENGAGEMENT = "STAKEHOLDER_ENGAGEMENT"
    """
    Stakeholder engagement.
    """
    SYNTHETIC_CONTENT_DETECTION_AND_LABELING = "SYNTHETIC_CONTENT_DETECTION_AND_LABELING"
    """
    Synthetic content detection and labeling tools and techniques.
    """
    WHISTLEBLOWER_PROTECTIONS = "WHISTLEBLOWER_PROTECTIONS"
    """
    Whistleblower protections.
    """
    WORKFORCE_DIVERSITY_AND_INTERDISCIPLINARY_TEAMS = "WORKFORCE_DIVERSITY_AND_INTERDISCIPLINARY_TEAMS"
    """
    Workforce diversity and interdisciplinary teams.
    """



class NamedThing(ConfiguredBaseModel):
    """
    Abstract base for identifiable elements of the GAI Profile.
    Inlined here to keep this schema standalone; mirrors the
    `NamedThing` defined in NIST AI 100-1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
         'in_subset': ['gai_base'],
         'related_mappings': ['nist_ai_100_1:NamedThing']})

    id: str = Field(default=..., description="""Unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""Human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:description'} })


class GaiRisk(NamedThing):
    """
    A risk that is novel to or exacerbated by Generative AI.
    Each instance corresponds to one of the 12 risk categories
    enumerated in NIST AI 600-1 Section 2.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['iso27001:Risk'],
         'close_mappings': ['nist_ai_100_1:AiSpecificRisk'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
         'in_subset': ['gai_core'],
         'related_mappings': ['iso29100:PrivacyRisk']})

    gai_risk_kind: Optional[GaiRiskCategoryEnum] = Field(default=None, description="""The GAI risk category this element represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk'], 'in_subset': ['gai_core']} })
    risk_categorization: Optional[GaiRiskCategorizationEnum] = Field(default=None, description="""Higher-level categorisation - technical/model, misuse, or
ecosystem/societal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk'], 'in_subset': ['gai_core']} })
    risk_scope: Optional[list[GaiRiskScopeEnum]] = Field(default=None, description="""Scope levels at which the risk may manifest.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk'], 'in_subset': ['gai_core']} })
    risk_sources: Optional[list[GaiRiskSourceEnum]] = Field(default=None, description="""Sources from which the risk may emerge.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk'], 'in_subset': ['gai_core']} })
    time_scale: Optional[list[GaiRiskTimeScaleEnum]] = Field(default=None, description="""Time scales over which the risk may materialise.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk'], 'in_subset': ['gai_core']} })
    lifecycle_stage: Optional[list[AiLifecycleStageEnum]] = Field(default=None, description="""AI lifecycle stage(s) at which a GAI risk may arise or at
which a suggested action applies (Section 2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk'],
         'in_subset': ['gai_base'],
         'related_mappings': ['nist_ai_100_1:lifecycle_stage']} })
    trustworthiness_characteristic: Optional[list[TrustworthinessCharacteristicEnum]] = Field(default=None, description="""Trustworthy AI Characteristic(s) most relevant to a GAI risk -
i.e., the \"Trustworthy AI Characteristics\" tag at the end of
each Section 2 risk description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk'],
         'in_subset': ['gai_base'],
         'related_mappings': ['nist_ai_100_1:trustworthiness_characteristic']} })
    addressed_by_actions: Optional[list[str]] = Field(default=None, description="""Suggested actions that address a GAI risk (back-reference
derived from `SuggestedAction.gai_risks`).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk'], 'in_subset': ['gai_core']} })
    id: str = Field(default=..., description="""Unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""Human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:description'} })


class SuggestedAction(NamedThing):
    """
    A suggested action an organisation can take to manage GAI
    risks. Each action is identified by an Action ID, linked to an
    AI RMF subcategory, and may be relevant to one or more GAI
    risks and AI actor tasks (NIST AI 600-1 Section 3).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['stix:CourseOfAction'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
         'in_subset': ['gai_actions'],
         'related_mappings': ['oscal_catalog:Control', 'gist_linkml:Task'],
         'slot_usage': {'description': {'description': 'The suggested-action text '
                                                       'itself.',
                                        'name': 'description'},
                        'id': {'description': 'Identifier for the action - typically '
                                              'the same as the\n'
                                              '`action_id` (e.g., "GV-1.1-001").',
                               'name': 'id'}}})

    action_id: str = Field(default=..., description="""Identifier of a Suggested Action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SuggestedAction'], 'in_subset': ['gai_actions']} })
    function_prefix: Optional[GaiActionFunctionPrefixEnum] = Field(default=None, description="""Two-letter function prefix of the action's subcategory.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SuggestedAction'], 'in_subset': ['gai_actions']} })
    applies_to_subcategory: Optional[str] = Field(default=None, description="""Identifier of the AI RMF subcategory the action applies to.""", json_schema_extra = { "linkml_meta": {'close_mappings': ['oscal_profile:Profile'],
         'domain_of': ['SuggestedAction'],
         'in_subset': ['gai_actions']} })
    gai_risks: Optional[list[GaiRiskCategoryEnum]] = Field(default=None, description="""GAI risk categories addressed by a suggested action or
considered by a primary consideration.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SuggestedAction'], 'in_subset': ['gai_core']} })
    actor_task: Optional[list[AiActorTaskEnum]] = Field(default=None, description="""Pertinent AI Actor Task(s) for a suggested action - i.e., the
\"AI Actor Tasks\" row at the bottom of each Section 3 table.""", json_schema_extra = { "linkml_meta": {'domain_of': ['SuggestedAction'],
         'in_subset': ['gai_base'],
         'related_mappings': ['nist_ai_100_1:actor_task']} })
    id: str = Field(default=..., description="""Identifier for the action - typically the same as the
`action_id` (e.g., \"GV-1.1-001\").""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""Human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""The suggested-action text itself.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:description'} })


class PrimaryGaiConsideration(NamedThing):
    """
    An overarching consideration derived from the NIST GAI PWG
    consultation process (Appendix A). The `consideration_kind`
    attribute discriminates between the four primary
    considerations: Governance, Pre-Deployment Testing, Content
    Provenance, and Incident Disclosure.

    All consideration-specific attributes are optional and apply
    to the appropriate `consideration_kind`:
      * GOVERNANCE: governance_practices, third_party_considerations
      * PRE_DEPLOYMENT_TESTING: limitations_of_current_approaches
      * CONTENT_PROVENANCE: provenance_techniques
      * INCIDENT_DISCLOSURE: ai_incident_definition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
         'in_subset': ['gai_considerations'],
         'related_mappings': ['nist_csf:CSFProperty']})

    consideration_kind: PrimaryConsiderationEnum = Field(default=..., description="""Which primary consideration this element represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrimaryGaiConsideration'], 'in_subset': ['gai_considerations']} })
    governance_practices: Optional[list[GovernancePracticeEnum]] = Field(default=None, description="""Governance plans and actions enumerated in NIST AI 600-1
Appendix A.1.2 (Organizational Governance).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrimaryGaiConsideration'], 'in_subset': ['gai_considerations']} })
    third_party_considerations: Optional[str] = Field(default=None, description="""Considerations for third-party GAI integrations, procurement,
SBOMs, SLAs, and SSAE reports (Appendix A.1.3).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrimaryGaiConsideration'], 'in_subset': ['gai_considerations']} })
    limitations_of_current_approaches: Optional[str] = Field(default=None, description="""For Pre-Deployment Testing: free-text discussion of why
current TEVV approaches may be inadequate (Appendix A.1.4).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrimaryGaiConsideration'], 'in_subset': ['gai_considerations']} })
    provenance_techniques: Optional[list[ProvenanceTechniqueEnum]] = Field(default=None, description="""For Content Provenance: provenance data tracking techniques
such as digital watermarking, metadata recording, digital
fingerprinting, and human authentication (Appendix A.1.6).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrimaryGaiConsideration'], 'in_subset': ['gai_considerations']} })
    ai_incident_definition: Optional[str] = Field(default=None, description="""For Incident Disclosure: the definition of AI incident used
by the organisation (Appendix A.1.8).""", json_schema_extra = { "linkml_meta": {'domain_of': ['PrimaryGaiConsideration'], 'in_subset': ['gai_considerations']} })
    id: str = Field(default=..., description="""Unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""Human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:description'} })


class StructuredPublicFeedback(NamedThing):
    """
    Methods used to evaluate whether GAI systems are performing as
    intended and to calibrate and verify traditional measurement
    methods (A.1.5).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
         'in_subset': ['gai_feedback'],
         'related_mappings': ['iso27001:InterestedParty']})

    feedback_method_kind: StructuredFeedbackMethodEnum = Field(default=..., description="""Which structured feedback method this element represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructuredPublicFeedback'], 'in_subset': ['gai_feedback']} })
    id: str = Field(default=..., description="""Unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""Human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:description'} })


class AiRedTeaming(StructuredPublicFeedback):
    """
    A structured testing exercise used to probe an AI system to
    find flaws and vulnerabilities such as inaccurate, harmful, or
    discriminatory outputs, often in a controlled environment and
    in collaboration with system developers (A.1.5).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
         'in_subset': ['gai_feedback'],
         'related_mappings': ['stix:AttackPattern'],
         'slot_usage': {'feedback_method_kind': {'ifabsent': 'StructuredFeedbackMethodEnum(AI_RED_TEAMING)',
                                                 'name': 'feedback_method_kind'}}})

    red_team_type: Optional[RedTeamingTypeEnum] = Field(default=None, description="""The type of AI red-teaming exercise.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRedTeaming'], 'in_subset': ['gai_feedback']} })
    feedback_method_kind: StructuredFeedbackMethodEnum = Field(default=StructuredFeedbackMethodEnum.AI_RED_TEAMING, description="""Which structured feedback method this element represents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['StructuredPublicFeedback'],
         'ifabsent': 'StructuredFeedbackMethodEnum(AI_RED_TEAMING)',
         'in_subset': ['gai_feedback']} })
    id: str = Field(default=..., description="""Unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""Human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:description'} })


class GaiProfile(NamedThing):
    """
    Root container that bundles the NIST AI 600-1 Generative AI
    Profile: GAI risks (Section 2), suggested actions (Section 3),
    and primary considerations (Appendix A). The GAI Profile is a
    *cross-sectoral* AI RMF profile (Section 1).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['nist_csf:CSFDocument'],
         'exact_mappings': ['oscal_profile:Profile'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
         'in_subset': ['gai_core'],
         'related_mappings': ['nist_ai_100_1:AiRmfProfile'],
         'tree_root': True})

    gai_risk_catalog: Optional[list[GaiRisk]] = Field(default=None, description="""The catalog of GAI risks (Section 2).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile'], 'in_subset': ['gai_core']} })
    suggested_actions: Optional[list[SuggestedAction]] = Field(default=None, description="""Suggested actions to manage GAI risks (Section 3).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile'], 'in_subset': ['gai_actions']} })
    primary_considerations: Optional[list[PrimaryGaiConsideration]] = Field(default=None, description="""The primary GAI considerations from Appendix A (Governance,
Pre-Deployment Testing, Content Provenance, Incident
Disclosure). Discriminated by `consideration_kind`.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile'], 'in_subset': ['gai_considerations']} })
    structured_feedback_methods: Optional[list[StructuredPublicFeedback]] = Field(default=None, description="""Structured public feedback methods relevant to the profile
(Appendix A.1.5).""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile'], 'in_subset': ['gai_feedback']} })
    id: str = Field(default=..., description="""Unique identifier for an element.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:identifier'} })
    title: Optional[str] = Field(default=None, description="""Human-readable title.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:title'} })
    description: Optional[str] = Field(default=None, description="""Free-text description.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NamedThing'],
         'in_subset': ['gai_base'],
         'slot_uri': 'dcterms:description'} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
NamedThing.model_rebuild()
GaiRisk.model_rebuild()
SuggestedAction.model_rebuild()
PrimaryGaiConsideration.model_rebuild()
StructuredPublicFeedback.model_rebuild()
AiRedTeaming.model_rebuild()
GaiProfile.model_rebuild()
