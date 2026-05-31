export type NamedThingId = string;
export type GaiRiskId = string;
export type SuggestedActionId = string;
export type PrimaryGaiConsiderationId = string;
export type StructuredPublicFeedbackId = string;
export type AiRedTeamingId = string;
export type GaiProfileId = string;
/**
* The seven characteristics of trustworthy AI systems described in
Figure 4 and Part 1 §3.
*/
export enum TrustworthinessCharacteristicEnum {
    
    /** Confirmation that requirements for a specific intended use have
been fulfilled (validation) and that the system performs as
required without failure (reliability). A necessary condition of
trustworthiness and the base for other characteristics. */
    VALID_AND_RELIABLE = "VALID_AND_RELIABLE",
    /** The system does not, under defined conditions, lead to a state
in which human life, health, property, or the environment is
endangered. */
    SAFE = "SAFE",
    /** The system can withstand unexpected adverse events or changes
(resilient) and maintain confidentiality, integrity, and
availability through protection mechanisms (secure). */
    SECURE_AND_RESILIENT = "SECURE_AND_RESILIENT",
    /** Trustworthy AI depends on accountability, which presupposes
transparency - the extent to which information about an AI
system and its outputs is available to those interacting with
it. */
    ACCOUNTABLE_AND_TRANSPARENT = "ACCOUNTABLE_AND_TRANSPARENT",
    /** Explainability concerns the mechanisms underlying an AI system's
operation; interpretability concerns the meaning of its output
in context. */
    EXPLAINABLE_AND_INTERPRETABLE = "EXPLAINABLE_AND_INTERPRETABLE",
    /** Norms and practices that help safeguard human autonomy,
identity, and dignity - including anonymity, confidentiality,
and control over personal information. */
    PRIVACY_ENHANCED = "PRIVACY_ENHANCED",
    /** Concerns for equality and equity by addressing issues such as
harmful bias and discrimination, and recognising that
perceptions of fairness differ across cultures and
applications. */
    FAIR_WITH_HARMFUL_BIAS_MANAGED = "FAIR_WITH_HARMFUL_BIAS_MANAGED",
};
/**
* AI lifecycle stages enumerated in NIST AI 600-1 Section 2:
"Risks can arise during design, development, deployment,
operation, and/or decommissioning." Distinct from the six-stage
`AiLifecycleStageEnum` of NIST AI 100-1 (see `related_mappings`).
*/
export enum GaiLifecycleStageEnum {
    
    /** Articulating system concept, objectives, requirements. */
    DESIGN = "DESIGN",
    /** Building, training, and tuning the GAI model or system. */
    DEVELOPMENT = "DEVELOPMENT",
    /** Placing the GAI system into a production environment. */
    DEPLOYMENT = "DEPLOYMENT",
    /** Running and monitoring the GAI system in use. */
    OPERATION = "OPERATION",
    /** Retiring or phasing out the GAI system. */
    DECOMMISSIONING = "DECOMMISSIONING",
};
/**
* AI Actor Tasks referenced by the Suggested Actions tables in
NIST AI 600-1 Section 3 (and defined in NIST AI 100-1
Appendix A).
*/
export enum GaiActorTaskEnum {
    
    /** Management, fiduciary, and legal authority for the organization. */
    GOVERNANCE_AND_OVERSIGHT = "GOVERNANCE_AND_OVERSIGHT",
    /** Concept, objectives, planning, design, and data collection. */
    AI_DESIGN = "AI_DESIGN",
    /** Model building, selection, calibration, training, and testing. */
    AI_DEVELOPMENT = "AI_DEVELOPMENT",
    /** Contextual decisions on how the AI system is used and deployed. */
    AI_DEPLOYMENT = "AI_DEPLOYMENT",
    /** Assessing accountability, bias, impacts, safety, liability, security. */
    AI_IMPACT_ASSESSMENT = "AI_IMPACT_ASSESSMENT",
    /** Operating the AI system and assessing system output and impacts. */
    OPERATION_AND_MONITORING = "OPERATION_AND_MONITORING",
    /** Test, Evaluation, Verification, and Validation tasks. */
    TEVV = "TEVV",
    /** Multidisciplinary practitioners with sector or context expertise. */
    DOMAIN_EXPERTS = "DOMAIN_EXPERTS",
    /** Individuals or groups using the AI system for specific purposes. */
    END_USERS = "END_USERS",
    /** Human-centered design practices and end-user involvement. */
    HUMAN_FACTORS = "HUMAN_FACTORS",
    /** Individuals, groups, or communities directly or indirectly affected. */
    AFFECTED_INDIVIDUALS_AND_COMMUNITIES = "AFFECTED_INDIVIDUALS_AND_COMMUNITIES",
    /** Acquisition of AI models, products, or services from third parties. */
    PROCUREMENT = "PROCUREMENT",
    /** Providers, developers, vendors, and evaluators external to the deploying organization. */
    THIRD_PARTY_ENTITIES = "THIRD_PARTY_ENTITIES",
};
/**
* The 12 risks unique to or exacerbated by Generative AI as
enumerated in NIST AI 600-1 Section 2.
*/
export enum GaiRiskCategoryEnum {
    
    /** Eased access to or synthesis of materially nefarious
information or design capabilities related to chemical,
biological, radiological, or nuclear (CBRN) weapons or
other dangerous materials or agents. */
    CBRN_INFORMATION_OR_CAPABILITIES = "CBRN_INFORMATION_OR_CAPABILITIES",
    /** The production of confidently stated but erroneous or
false content (colloquially "hallucinations" or
"fabrications") by which users may be misled or deceived. */
    CONFABULATION = "CONFABULATION",
    /** Eased production of and access to violent, inciting,
radicalizing, or threatening content as well as
recommendations to carry out self-harm or conduct illegal
activities. Includes difficulty controlling public
exposure to hateful and disparaging or stereotyping
content. */
    DANGEROUS_VIOLENT_OR_HATEFUL_CONTENT = "DANGEROUS_VIOLENT_OR_HATEFUL_CONTENT",
    /** Impacts due to leakage and unauthorized use, disclosure, or
de-anonymization of biometric, health, location, or other
personally identifiable information or sensitive data. */
    DATA_PRIVACY = "DATA_PRIVACY",
    /** Impacts due to high compute resource utilization in
training or operating GAI models, and related outcomes that
may adversely impact ecosystems. */
    ENVIRONMENTAL_IMPACTS = "ENVIRONMENTAL_IMPACTS",
    /** Amplification and exacerbation of historical, societal,
and systemic biases; performance disparities between
sub-groups or languages, possibly due to non-representative
training data, resulting in discrimination, amplification
of biases, or incorrect presumptions about performance;
undesired homogeneity that skews system or model outputs. */
    HARMFUL_BIAS_OR_HOMOGENIZATION = "HARMFUL_BIAS_OR_HOMOGENIZATION",
    /** Arrangements of or interactions between a human and an AI
system which can result in the human inappropriately
anthropomorphising GAI systems or experiencing algorithmic
aversion, automation bias, over-reliance, or emotional
entanglement with GAI systems. */
    HUMAN_AI_CONFIGURATION = "HUMAN_AI_CONFIGURATION",
    /** Lowered barrier to entry to generate and support the
exchange and consumption of content which may not
distinguish fact from opinion or fiction or acknowledge
uncertainties, or could be leveraged for large-scale
dis- and mis-information campaigns. */
    INFORMATION_INTEGRITY = "INFORMATION_INTEGRITY",
    /** Lowered barriers for offensive cyber capabilities,
including via automated discovery and exploitation of
vulnerabilities; increased attack surface for targeted
cyberattacks, which may compromise a system's availability
or the confidentiality or integrity of training data,
code, or model weights. */
    INFORMATION_SECURITY = "INFORMATION_SECURITY",
    /** Eased production or replication of alleged copyrighted,
trademarked, or licensed content without authorization
(possibly outside fair use); eased exposure of trade
secrets; or plagiarism or illegal replication. */
    INTELLECTUAL_PROPERTY = "INTELLECTUAL_PROPERTY",
    /** Eased production of and access to obscene, degrading,
and/or abusive imagery which can cause harm, including
synthetic child sexual abuse material (CSAM) and
nonconsensual intimate images (NCII) of adults. */
    OBSCENE_DEGRADING_OR_ABUSIVE_CONTENT = "OBSCENE_DEGRADING_OR_ABUSIVE_CONTENT",
    /** Non-transparent or untraceable integration of upstream
third-party components, including data that has been
improperly obtained or not processed and cleaned due to
increased automation from GAI; improper supplier vetting
across the AI lifecycle; or other issues that diminish
transparency or accountability for downstream users. */
    VALUE_CHAIN_AND_COMPONENT_INTEGRATION = "VALUE_CHAIN_AND_COMPONENT_INTEGRATION",
};
/**
* Higher-level grouping of GAI risks, derived from the UK's
International Scientific Report on the Safety of Advanced AI
(NIST AI 600-1 Section 2, footnote 5).
*/
export enum GaiRiskCategorizationEnum {
    
    /** Risks from malfunction. Examples include confabulation;
dangerous or violent recommendations; data privacy; value
chain and component integration; harmful bias and
homogenization. */
    TECHNICAL_OR_MODEL_RISKS = "TECHNICAL_OR_MODEL_RISKS",
    /** Risks from malicious use. Examples include CBRN information
or capabilities; data privacy; human-AI configuration;
obscene, degrading, and/or abusive content; information
integrity; information security. */
    MISUSE_BY_HUMANS = "MISUSE_BY_HUMANS",
    /** Systemic risks. Examples include data privacy;
environmental impacts; intellectual property. */
    ECOSYSTEM_OR_SOCIETAL_RISKS = "ECOSYSTEM_OR_SOCIETAL_RISKS",
};
/**
* The scope at which a GAI risk may manifest (Section 2).
*/
export enum GaiRiskScopeEnum {
    
    /** Individual GAI model or system level. */
    MODEL_OR_SYSTEM = "MODEL_OR_SYSTEM",
    /** Specific application or implementation - i.e., a particular
use case. */
    APPLICATION_OR_IMPLEMENTATION = "APPLICATION_OR_IMPLEMENTATION",
    /** Beyond a single system or organizational context - e.g.,
algorithmic monocultures, labor-market impacts, creative
economies. */
    ECOSYSTEM = "ECOSYSTEM",
};
/**
* The source(s) from which a GAI risk may emerge (Section 2).
*/
export enum GaiRiskSourceEnum {
    
    /** From decisions made during model or system design. */
    DESIGN = "DESIGN",
    /** From the training data or training process. */
    TRAINING = "TRAINING",
    /** From operating the GAI model or system. */
    OPERATION = "OPERATION",
    /** From inputs supplied to the model at inference time. */
    MODEL_INPUTS = "MODEL_INPUTS",
    /** From the GAI system's generated outputs. */
    MODEL_OUTPUTS = "MODEL_OUTPUTS",
    /** From human behaviour - abuse, misuse, or unsafe repurposing
by humans (adversarial or not). */
    HUMAN_BEHAVIOR = "HUMAN_BEHAVIOR",
    /** From interactions between a human and the AI system. */
    HUMAN_AI_INTERACTION = "HUMAN_AI_INTERACTION",
};
/**
* The time scale over which a GAI risk may materialise
(Section 2).
*/
export enum GaiRiskTimeScaleEnum {
    
    /** Materialises abruptly (e.g., distribution of deepfakes). */
    IMMEDIATE = "IMMEDIATE",
    /** Materialises across extended periods (e.g., long-term
effect of disinformation on societal trust). */
    PROLONGED = "PROLONGED",
};
/**
* Two-letter function prefix used in GAI Action IDs.
*/
export enum GaiActionFunctionPrefixEnum {
    
    /** Govern function. */
    GV = "GV",
    /** Map function. */
    MP = "MP",
    /** Measure function. */
    MS = "MS",
    /** Manage function. */
    MG = "MG",
};
/**
* The four overarching themes derived from the GAI PWG
consultation process (Appendix A).
*/
export enum PrimaryConsiderationEnum {
    
    /** How organizational governance regimes may be re-evaluated
and adjusted for GAI contexts (A.1). */
    GOVERNANCE = "GOVERNANCE",
    /** Test, evaluation, validation, and verification practices
appropriate for GAI prior to deployment (A.1.4). */
    PRE_DEPLOYMENT_TESTING = "PRE_DEPLOYMENT_TESTING",
    /** Digital transparency mechanisms (provenance data tracking,
watermarking, synthetic content detection) for tracing
origin and history of content (A.1.6 - A.1.7). */
    CONTENT_PROVENANCE = "CONTENT_PROVENANCE",
    /** Documenting, reporting, and sharing information about AI
incidents to mitigate harm and improve risk management
(A.1.8). */
    INCIDENT_DISCLOSURE = "INCIDENT_DISCLOSURE",
};
/**
* Categories of structured public feedback for GAI risk
management (Appendix A.1.5).
*/
export enum StructuredFeedbackMethodEnum {
    
    /** Methods used to solicit feedback from civil society groups,
affected communities, and users (focus groups, small user
studies, surveys). */
    PARTICIPATORY_ENGAGEMENT_METHODS = "PARTICIPATORY_ENGAGEMENT_METHODS",
    /** Methods used to determine how people interact with,
consume, use, and make sense of AI-generated information
(UX, usability, randomised experiments). */
    FIELD_TESTING = "FIELD_TESTING",
    /** A structured testing exercise used to probe an AI system
to find flaws and vulnerabilities such as inaccurate,
harmful, or discriminatory outputs. */
    AI_RED_TEAMING = "AI_RED_TEAMING",
};
/**
* Types of AI red-teaming exercises (Appendix A.1.5).
*/
export enum RedTeamingTypeEnum {
    
    /** Performed by general users not necessarily having AI or
technical expertise. */
    GENERAL_PUBLIC = "GENERAL_PUBLIC",
    /** Performed by specialists with expertise in the domain or
specific red-teaming context (medicine, biotech,
cybersecurity). */
    EXPERT = "EXPERT",
    /** Hybrid exercises using both expert and general-public
participants. */
    COMBINATION = "COMBINATION",
    /** Performed by GAI in combination with specialist or
non-specialist human teams. */
    HUMAN_AND_AI = "HUMAN_AND_AI",
};
/**
* Provenance data tracking techniques for GAI content
(Appendix A.1.6). "Some well-known techniques for provenance
data tracking include digital watermarking, metadata
recording, digital fingerprinting, and human authentication,
among others."
*/
export enum ProvenanceTechniqueEnum {
    
    /** Overt or covert digital watermarks embedded in content to
allow downstream verification of origin. */
    DIGITAL_WATERMARKING = "DIGITAL_WATERMARKING",
    /** Recording metadata about content (creator, date/time,
location, modifications, sources) for text, image, video,
audio, or underlying datasets. */
    METADATA_RECORDING = "METADATA_RECORDING",
    /** Computing a content-derived identifier that can be matched
against a reference store to detect known content. */
    DIGITAL_FINGERPRINTING = "DIGITAL_FINGERPRINTING",
    /** Human-mediated verification of content origin or
authenticity. */
    HUMAN_AUTHENTICATION = "HUMAN_AUTHENTICATION",
};
/**
* Governance plans and actions for GAI systems enumerated in
NIST AI 600-1 Appendix A.1.2 ("Organizational Governance").
*/
export enum GovernancePracticeEnum {
    
    /** Accessibility and reasonable accommodations. */
    ACCESSIBILITY_AND_REASONABLE_ACCOMMODATIONS = "ACCESSIBILITY_AND_REASONABLE_ACCOMMODATIONS",
    /** AI actor credentials and qualifications. */
    AI_ACTOR_CREDENTIALS_AND_QUALIFICATIONS = "AI_ACTOR_CREDENTIALS_AND_QUALIFICATIONS",
    /** Alignment to organizational values. */
    ALIGNMENT_TO_ORGANIZATIONAL_VALUES = "ALIGNMENT_TO_ORGANIZATIONAL_VALUES",
    /** Auditing and assessment. */
    AUDITING_AND_ASSESSMENT = "AUDITING_AND_ASSESSMENT",
    /** Change-management controls. */
    CHANGE_MANAGEMENT_CONTROLS = "CHANGE_MANAGEMENT_CONTROLS",
    /** Commercial use governance. */
    COMMERCIAL_USE = "COMMERCIAL_USE",
    /** Data provenance. */
    DATA_PROVENANCE = "DATA_PROVENANCE",
    /** Data protection. */
    DATA_PROTECTION = "DATA_PROTECTION",
    /** Data retention. */
    DATA_RETENTION = "DATA_RETENTION",
    /** Consistency in use of defining key terms. */
    CONSISTENCY_IN_USE_OF_DEFINING_KEY_TERMS = "CONSISTENCY_IN_USE_OF_DEFINING_KEY_TERMS",
    /** Decommissioning practices. */
    DECOMMISSIONING = "DECOMMISSIONING",
    /** Discouraging anonymous use. */
    DISCOURAGING_ANONYMOUS_USE = "DISCOURAGING_ANONYMOUS_USE",
    /** Education on GAI risks and responsible use. */
    EDUCATION = "EDUCATION",
    /** Impact assessments. */
    IMPACT_ASSESSMENTS = "IMPACT_ASSESSMENTS",
    /** Incident response procedures. */
    INCIDENT_RESPONSE = "INCIDENT_RESPONSE",
    /** Ongoing monitoring of GAI systems. */
    MONITORING = "MONITORING",
    /** User opt-out mechanisms. */
    OPT_OUTS = "OPT_OUTS",
    /** Risk-based controls. */
    RISK_BASED_CONTROLS = "RISK_BASED_CONTROLS",
    /** Risk mapping and measurement. */
    RISK_MAPPING_AND_MEASUREMENT = "RISK_MAPPING_AND_MEASUREMENT",
    /** Science-backed test, evaluation, validation, and verification practices. */
    SCIENCE_BACKED_TEVV_PRACTICES = "SCIENCE_BACKED_TEVV_PRACTICES",
    /** Secure software development practices. */
    SECURE_SOFTWARE_DEVELOPMENT_PRACTICES = "SECURE_SOFTWARE_DEVELOPMENT_PRACTICES",
    /** Stakeholder engagement. */
    STAKEHOLDER_ENGAGEMENT = "STAKEHOLDER_ENGAGEMENT",
    /** Synthetic content detection and labeling tools and techniques. */
    SYNTHETIC_CONTENT_DETECTION_AND_LABELING = "SYNTHETIC_CONTENT_DETECTION_AND_LABELING",
    /** Whistleblower protections. */
    WHISTLEBLOWER_PROTECTIONS = "WHISTLEBLOWER_PROTECTIONS",
    /** Workforce diversity and interdisciplinary teams. */
    WORKFORCE_DIVERSITY_AND_INTERDISCIPLINARY_TEAMS = "WORKFORCE_DIVERSITY_AND_INTERDISCIPLINARY_TEAMS",
};


/**
 * A generic grouping for any identifiable AI RMF element.
 */
export interface NamedThing {
    /** A unique identifier for an element. */
    id: string,
    /** A short human-readable name. */
    name?: string,
    /** A human-readable title. */
    title?: string,
    /** A human-readable description. */
    description?: string,
    /** Related references. */
    see_also?: string[],
}


/**
 * A risk that is novel to or exacerbated by Generative AI.
Each instance corresponds to one of the 12 risk categories
enumerated in NIST AI 600-1 Section 2.
 */
export interface GaiRisk extends NamedThing {
    /** The GAI risk category this element represents. */
    gai_risk_kind?: string,
    /** Higher-level categorisation - technical/model, misuse, or
ecosystem/societal. */
    risk_categorization?: string,
    /** Scope levels at which the risk may manifest. */
    risk_scope?: string,
    /** Sources from which the risk may emerge. */
    risk_sources?: string,
    /** Time scales over which the risk may materialise. */
    time_scale?: string,
    /** Trustworthiness characteristic(s) the element pertains to. */
    trustworthiness_characteristic?: string,
    /** Suggested actions that address a GAI risk (back-reference
derived from `SuggestedAction.gai_risks`). */
    addressed_by_actions?: SuggestedActionId[],
    /** AI lifecycle stage(s) at which the GAI risk may arise
(NIST AI 600-1 Section 2). Uses the GAI five-stage
lifecycle (`GaiLifecycleStageEnum`). */
    lifecycle_stage?: string,
}


/**
 * A suggested action an organisation can take to manage GAI
risks. Each action is identified by an Action ID, linked to an
AI RMF subcategory, and may be relevant to one or more GAI
risks and AI actor tasks (NIST AI 600-1 Section 3).
 */
export interface SuggestedAction extends NamedThing {
    /** Identifier of a Suggested Action. */
    action_id: string,
    /** Two-letter function prefix of the action's subcategory. */
    function_prefix?: string,
    /** Identifier of the AI RMF subcategory the action applies to. */
    applies_to_subcategory?: string,
    /** GAI risk categories addressed by a suggested action or
considered by a primary consideration. */
    gai_risks?: string,
    /** Pertinent AI Actor Task(s) for the suggested action - i.e.,
the "AI Actor Tasks" row at the bottom of each Section 3
table. */
    actor_task?: string,
}


/**
 * An overarching consideration derived from the NIST GAI PWG
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
 */
export interface PrimaryGaiConsideration extends NamedThing {
    /** Which primary consideration this element represents. */
    consideration_kind: string,
    /** Governance plans and actions enumerated in NIST AI 600-1
Appendix A.1.2 (Organizational Governance). */
    governance_practices?: string,
    /** Considerations for third-party GAI integrations, procurement,
SBOMs, SLAs, and SSAE reports (Appendix A.1.3). */
    third_party_considerations?: string,
    /** For Pre-Deployment Testing: free-text discussion of why
current TEVV approaches may be inadequate (Appendix A.1.4). */
    limitations_of_current_approaches?: string,
    /** For Content Provenance: provenance data tracking techniques
such as digital watermarking, metadata recording, digital
fingerprinting, and human authentication (Appendix A.1.6). */
    provenance_techniques?: string,
    /** For Incident Disclosure: the definition of AI incident used
by the organisation (Appendix A.1.8). */
    ai_incident_definition?: string,
}


/**
 * Methods used to evaluate whether GAI systems are performing as
intended and to calibrate and verify traditional measurement
methods (A.1.5).
 */
export interface StructuredPublicFeedback extends NamedThing {
    /** Which structured feedback method this element represents. */
    feedback_method_kind: string,
}


/**
 * A structured testing exercise used to probe an AI system to
find flaws and vulnerabilities such as inaccurate, harmful, or
discriminatory outputs, often in a controlled environment and
in collaboration with system developers (A.1.5).
 */
export interface AiRedTeaming extends StructuredPublicFeedback {
    /** The type of AI red-teaming exercise. */
    red_team_type?: string,
}


/**
 * Root container that bundles the NIST AI 600-1 Generative AI
Profile: GAI risks (Section 2), suggested actions (Section 3),
and primary considerations (Appendix A). The GAI Profile is a
*cross-sectoral* AI RMF profile (Section 1).
 */
export interface GaiProfile extends NamedThing {
    /** The catalog of GAI risks (Section 2). */
    gai_risk_catalog?: GaiRisk[],
    /** Suggested actions to manage GAI risks (Section 3). */
    suggested_actions?: SuggestedAction[],
    /** The primary GAI considerations from Appendix A (Governance,
Pre-Deployment Testing, Content Provenance, Incident
Disclosure). Discriminated by `consideration_kind`. */
    primary_considerations?: PrimaryGaiConsideration[],
    /** Structured public feedback methods relevant to the profile
(Appendix A.1.5). */
    structured_feedback_methods?: StructuredPublicFeedback[],
}



