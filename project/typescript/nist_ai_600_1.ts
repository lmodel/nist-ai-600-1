export type AiRmfRecordAiRmfId = string;
export type AiRmfProfileAiRmfId = string;
export type GaiProfileAiRmfId = string;
/**
* The seven characteristics of trustworthy AI systems in section 3 of the publication.
*/
export enum AiRmfCharacteristicName {
    
    /** Shown by evidence to meet the needs of its intended use, and works without failure over time. Figure 4 makes it a necessary condition for the others. */
    Valid_and_Reliable = "valid_and_reliable",
    /** Keeps people, property and the environment out of danger under defined conditions. */
    Safe = "safe",
    /** Withstands adverse events and recovers from them, and keeps confidentiality, integrity and availability through protections against attack. */
    Secure_and_Resilient = "secure_and_resilient",
    /** Answerable for outcomes, which rests on people being able to get information about the system and its outputs. Figure 4 shows it relating to all the others. */
    Accountable_and_Transparent = "accountable_and_transparent",
    /** Its working can be represented (how a decision was made) and its output understood in context (why, and what it means for the user). */
    Explainable_and_Interpretable = "explainable_and_interpretable",
    /** Guided by the norms and practices that protect human autonomy, identity and dignity, such as anonymity, confidentiality and control. */
    Privacy_Enhanced = "privacy_enhanced",
    /** Addresses equality and equity, including harmful bias and discrimination, knowing that views of fairness differ across cultures and applications. */
    Fair_EN_DASH_with_Harmful_Bias_Managed = "fair_with_harmful_bias_managed",
};
/**
* The ten AI actor tasks and five additional AI actors of Appendix A.
*/
export enum AiRmfActorTaskName {
    
    /** Setting what the system is for, planning and designing it, and gathering and preparing its data. */
    AI_Design = "ai_design",
    /** Providing the initial infrastructure, and creating, selecting, calibrating, training and testing models. */
    AI_Development = "ai_development",
    /** Deciding how the system is used and putting it into production, including pilots and compliance checks. */
    AI_Deployment = "ai_deployment",
    /** Running the system and regularly assessing its output and impacts. */
    Operation_and_Monitoring = "operation_and_monitoring",
    /** Examining the system or its components and finding and fixing problems, throughout the lifecycle. */
    Test_Evaluation_Verification_and_Validation_LEFT_PARENTHESISTEVVRIGHT_PARENTHESIS = "tevv",
    /** Human-centered design and evaluation, involving end users and bringing context-specific norms and values into design. */
    Human_Factors = "human_factors",
    /** Giving knowledge of the sector or setting where the system is used. */
    Domain_Expert = "domain_expert",
    /** Assessing accountability, harmful bias, impacts, product safety, liability and security. */
    AI_Impact_Assessment = "ai_impact_assessment",
    /** Acquiring AI from another party, under financial, legal or policy authority. */
    Procurement = "procurement",
    /** Holding management, fiduciary and legal authority for the organization where the system is designed, developed or deployed. */
    Governance_and_Oversight = "governance_and_oversight",
    /** Outside organizations that supply or evaluate the data, models, systems or services an organization acquires. */
    Third_party_entities = "third_party_entities",
    /** The people or groups who use the system, whether new to technology or expert in AI. */
    End_users = "end_users",
    /** Those directly or indirectly affected by the system or its output, whether or not they interact with it. */
    Affected_individualsSOLIDUScommunities = "affected_individuals_and_communities",
    /** Those who may provide norms or guidance on AI risk, such as standards bodies, advocacy groups and researchers. */
    Other_AI_actors = "other_ai_actors",
    /** Those most likely to experience the impacts directly, who may motivate what other AI actors do. */
    General_public = "general_public",
};
/**
* The kinds of AI RMF profile that section 6 names.
*/
export enum AiRmfProfileKind {
    
    /** The Core implemented for a specific setting or application. */
    Use_case_profile = "use_case",
    /** A temporal profile saying how AI is managed today and the related risks, in terms of current outcomes. */
    Current_Profile = "current",
    /** A temporal profile saying which outcomes the desired risk management goals need. */
    Target_Profile = "target",
    /** Covers risks of models or applications used across use cases or sectors, or activities common to them, such as using large language models. */
    Cross_sectoral_profile = "cross_sectoral",
};
/**
* The 12 risks of section 2.
*/
export enum GaiRiskName {
    
    /** Easier access to dangerous information or design abilities for chemical, biological, radiological or nuclear weapons. */
    CBRN_Information_or_Capabilities = "cbrn_information_or_capabilities",
    /** Confident but wrong output that can mislead users. */
    Confabulation = "confabulation",
    /** Easier production of content that incites or threatens, recommends harm, or disparages. */
    Dangerous_Violent_or_Hateful_Content = "dangerous_violent_or_hateful_content",
    /** Leaks, misuse or de-anonymization of personal or sensitive data. */
    Data_Privacy = "data_privacy",
    /** Effects on ecosystems from the heavy computing that training and operating models need. */
    Environmental_Impacts = "environmental_impacts",
    /** Worse systemic bias, unequal performance across groups or languages, and output skewed by sameness. */
    Harmful_Bias_or_Homogenization = "harmful_bias_or_homogenization",
    /** Interaction that leads people to over-rely on, anthropomorphize or become entangled with a system, or to distrust it. */
    Human_AI_Configuration = "human_ai_configuration",
    /** Easier creation and spread of content that blurs fact and opinion, or that can drive large disinformation campaigns. */
    Information_Integrity = "information_integrity",
    /** Easier offensive cyber activity, and a larger attack surface on a system, its data, code or weights. */
    Information_Security = "information_security",
    /** Easier unauthorized copying of protected content, exposure of trade secrets, and plagiarism. */
    Intellectual_Property = "intellectual_property",
    /** Easier production of harmful imagery, including synthetic abuse material and intimate images without consent. */
    Obscene_Degrading_andSOLIDUSor_Abusive_Content = "obscene_degrading_or_abusive_content",
    /** Opaque use of third-party components and data, and poor supplier vetting, that weaken accountability downstream. */
    Value_Chain_and_Component_Integration = "value_chain_and_component_integration",
};
/**
* The three groups into which footnote 5 says an organization could sort the risks, as one possible way.
*/
export enum GaiRiskGrouping {
    
    /** Risks from malfunction. */
    Technical_SOLIDUS_Model_risks = "technical_or_model",
    /** Risks from malicious use. */
    Misuse_by_humans = "misuse_by_humans",
    /** Systemic risks. */
    Ecosystem_SOLIDUS_societal_risks = "ecosystem_or_societal",
};
/**
* The lifecycle stages section 2 names for GAI. They differ from the seven stages of the AI RMF's Figure 3.
*/
export enum GaiLifecycleStage {
    
    /** Setting out the system before it is built. */
    Design = "design",
    /** Building and training it. */
    Development = "development",
    /** Putting it into use. */
    Deployment = "deployment",
    /** Running it. */
    Operation = "operation",
    /** Retiring it. */
    Decommissioning = "decommissioning",
};
/**
* The levels where section 2 says a risk may exist.
*/
export enum GaiRiskScope {
    
    /** The level of one model or system. */
    Model_or_system = "model_or_system",
    /** The level of one specific use case. */
    Application_or_implementation = "application_or_implementation",
    /** Beyond one system or organization, such as algorithmic monocultures or effects on labor markets. */
    Ecosystem = "ecosystem",
};
/**
* Where section 2 says a risk may come from.
*/
export enum GaiRiskSource {
    
    /** The design of the model itself. */
    Design = "design",
    /** The training of the model. */
    Training = "training",
    /** The operation of the model. */
    Operation = "operation",
    /** What goes into the model or system. */
    Inputs = "inputs",
    /** What the system produces. */
    Outputs = "outputs",
    /** Abuse, misuse or unsafe repurposing by people, whether adversarial or not. */
    Human_behavior = "human_behavior",
    /** How a person and a system act on each other. */
    Human_AI_interaction = "human_ai_interaction",
};
/**
* How section 2 says a risk may materialize over time.
*/
export enum GaiRiskTimeScale {
    
    /** All at once, such as immediate emotional harm from a harmful deepfake image. */
    Abruptly = "abrupt",
    /** Slowly, such as the long-term effect of disinformation on trust in institutions. */
    Across_extended_periods = "extended",
};
/**
* The plans and actions that section A.1.2 says apply to GAI from other AI governance.
*/
export enum GaiGovernancePlan {
    
    Accessibility_and_reasonable_accommodations = "accessibility_and_reasonable_accommodations",
    AI_actor_credentials_and_qualifications = "ai_actor_credentials_and_qualifications",
    Alignment_to_organizational_values = "alignment_to_organizational_values",
    Auditing_and_assessment = "auditing_and_assessment",
    Change_management_controls = "change_management_controls",
    Commercial_use = "commercial_use",
    Data_provenance = "data_provenance",
    Data_protection = "data_protection",
    Data_retention = "data_retention",
    Consistency_in_use_of_defining_key_terms = "consistency_in_use_of_defining_key_terms",
    Decommissioning = "decommissioning",
    Discouraging_anonymous_use = "discouraging_anonymous_use",
    Education = "education",
    Impact_assessments = "impact_assessments",
    Incident_response = "incident_response",
    Monitoring = "monitoring",
    Opt_outs = "opt_outs",
    Risk_based_controls = "risk_based_controls",
    Risk_mapping_and_measurement = "risk_mapping_and_measurement",
    Science_backed_TEVV_practices = "science_backed_tevv_practices",
    Secure_software_development_practices = "secure_software_development_practices",
    Stakeholder_engagement = "stakeholder_engagement",
    Synthetic_content_detection_and_labeling_tools_and_techniques = "synthetic_content_detection_and_labeling_tools_and_techniques",
    Whistleblower_protections = "whistleblower_protections",
    Workforce_diversity_and_interdisciplinary_teams = "workforce_diversity_and_interdisciplinary_teams",
};
/**
* The existing controls that section A.1.3 says can apply to third-party GAI.
*/
export enum GaiThirdPartyControl {
    
    /** Checking a provider before acquiring its GAI technology or data. */
    Acquisition_and_procurement_due_diligence = "acquisition_and_procurement_due_diligence",
    /** Asking a provider what its software is made of. */
    Requests_for_software_bills_of_materials = "software_bills_of_materials",
    /** Holding a provider to agreed levels of service. */
    Application_of_service_level_agreements = "service_level_agreements",
    /** Asking for a provider's attestation reports. */
    Statement_on_standards_for_attestation_engagement_reports = "ssae_reports",
};
/**
* The types of AI red-teaming in section A.1.5.
*/
export enum GaiRedTeamingType {
    
    /** By general users who are not necessarily AI or technical experts. */
    General_Public = "general_public",
    /** By specialists in the domain or the context of use. */
    Expert = "expert",
    /** By both experts and general public participants. */
    Combination = "combination",
    /** By GAI together with human teams, specialist or not. */
    Human_SOLIDUS_AI = "human_ai",
};
/**
* The techniques for provenance data tracking in section A.1.6.
*/
export enum GaiProvenanceTechnique {
    
    /** Placing visible or hidden marks on content. */
    Digital_watermarking = "digital_watermarking",
    /** Recording facts about the content, such as its creator, date and sources. */
    Metadata_recording = "metadata_recording",
    /** Identifying content from its own characteristics. */
    Digital_fingerprinting = "digital_fingerprinting",
    /** Having people confirm where content came from. */
    Human_authentication = "human_authentication",
};
/**
* The kinds of harm that section A.1.8's definition of an AI incident names.
*/
export enum GaiIncidentHarm {
    
    /** To a person or group, including psychological harm and harm to mental health. */
    Injury_or_harm_to_health = "injury_or_harm_to_health",
    /** To its management and operation. */
    Disruption_of_critical_infrastructure = "critical_infrastructure_disruption",
    /** Of human rights, or of obligations under law that protects fundamental, labor and intellectual property rights. */
    Violations_of_rights_or_legal_obligations = "rights_violations",
    /** To things and groups beyond the individual. */
    Harm_to_property_communities_or_the_environment = "harm_to_property_communities_or_environment",
};


/**
 * The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct from what the publication itself lists.
 */
export interface AiRmfRecord {
    /** The identifier an adopter gives a record of its own. */
    ai_rmf_id: string,
    /** The element's name. */
    title?: string,
    /** What the element says or is. */
    description?: string,
}


/**
 * An implementation of the Core's functions, categories and subcategories for a setting, application or technology, based on the adopter's requirements, risk tolerance and resources.
 */
export interface AiRmfProfile extends AiRmfRecord {
    /** Which of the publication's kinds of profile this is. A current profile for one use case is both. */
    ai_rmf_profile_kinds: string,
    /** The sector, industry, technology, organization or end use the profile covers, such as hiring. */
    ai_rmf_profile_setting?: string,
    /** The subcategories the profile selects. An adopter may select from them rather than apply all. */
    ai_rmf_profile_subcategories?: string[],
}


/**
 * A risk that section 2 defines as unique to or made worse by the development and use of GAI.
 */
export interface GaiRisk {
    /** The risk's definition in section 2. */
    description?: string,
    /** Which of the 12 risks this is. */
    gai_risk_name: string,
    /** The subsection of section 2 that discusses the risk, such as 2.1. */
    gai_risk_section: string,
    /** The AI RMF's trustworthiness characteristics that the subsection names for the risk. */
    gai_risk_characteristics?: string,
    /** The groups footnote 5 suggests for the risk. The footnote lists Data Privacy under all three. */
    gai_risk_groupings?: string,
    /** The lifecycle stages where the risk can arise for the adopter's model, system or use case. */
    gai_risk_lifecycle_stages?: string,
    /** The levels where the risk exists for the adopter's model, system or use case. */
    gai_risk_scopes?: string,
    /** Where the risk comes from for the adopter's model, system or use case. */
    gai_risk_sources?: string,
    /** How the risk materializes over time for the adopter's model, system or use case. */
    gai_risk_time_scales?: string,
}


/**
 * An AI RMF subcategory as one table of section 3 addresses it. The Profile covers only some of the 72.
 */
export interface GaiSubcategory {
    /** The subcategory's identifier, such as GOVERN 1.1. */
    ai_rmf_subcategory_id: string,
    /** The subcategory's statement as the table restates it. */
    description: string,
    /** The suggested actions the table lists. */
    gai_subcategory_actions: GaiSuggestedAction[],
    /** The AI actor tasks the table names. They belong to the table and not to one action: the publication says not every task applies to every action. */
    gai_subcategory_actor_tasks?: string,
}


/**
 * A step an organization or AI actor can take to manage GAI risks, which one row of a table states.
 */
export interface GaiSuggestedAction {
    /** The action's identifier, such as GV-1.1-001. */
    gai_action_id: string,
    /** The action's text in the table. */
    description: string,
    /** The GAI risks the row tags the action with. */
    gai_action_risks?: string,
}


/**
 * One of the four primary considerations of Appendix A, which also inform the suggested actions.
 */
export interface GaiPrimaryConsideration {
    /** Which of the four classes this record is. */
    gai_consideration_type: string,
    /** The element's name. */
    title: string,
    /** What the element says or is. */
    description?: string,
    /** The subsections of Appendix A that discuss the consideration, such as A.1.2. */
    gai_consideration_sections?: string[],
}


/**
 * How an organization's governance can be revisited for GAI, including across the AI value chain.
 */
export interface GaiGovernanceConsideration extends GaiPrimaryConsideration {
    /** The plans and actions that section A.1.2 lists from other AI governance. */
    gai_governance_plans?: string,
    /** The existing controls that section A.1.3 says can apply to third-party GAI. */
    gai_third_party_controls?: string,
}


/**
 * How GAI can be tested before deployment while better approaches mature, and where current tests fall short.
 */
export interface GaiPreDeploymentTestingConsideration extends GaiPrimaryConsideration {
    /** The kinds of structured public feedback section A.1.5 gives as examples. */
    gai_structured_feedback?: GaiStructuredFeedback[],
}


/**
 * How tracking the origin and history of content helps tell authentic content from synthetic content.
 */
export interface GaiContentProvenanceConsideration extends GaiPrimaryConsideration {
    /** The well-known techniques for provenance data tracking that section A.1.6 names. */
    gai_provenance_techniques?: string,
}


/**
 * How documenting, reporting and sharing AI incidents helps prevent harm, though no formal channels exist.
 */
export interface GaiIncidentDisclosureConsideration extends GaiPrimaryConsideration {
    /** The kinds of harm that section A.1.8's definition of an AI incident names. */
    gai_incident_harms?: string,
}


/**
 * A way of using structured public feedback to evaluate whether GAI systems perform as intended.
 */
export interface GaiStructuredFeedback {
    /** Which of the three classes this record is. */
    gai_feedback_type: string,
    /** The element's name. */
    title: string,
    /** What the element says or is. */
    description?: string,
}


/**
 * Asking civil society groups, affected communities and users for feedback, such as through focus groups or surveys.
 */
export interface GaiParticipatoryEngagement extends GaiStructuredFeedback {
}


/**
 * Structured settings that show how people interact with and use AI-generated information.
 */
export interface GaiFieldTesting extends GaiStructuredFeedback {
}


/**
 * A structured exercise that probes an AI system for flaws and vulnerabilities, often with its developers.
 */
export interface GaiAiRedTeaming extends GaiStructuredFeedback {
    /** The kinds of AI red-teaming that may suit the use case. */
    gai_red_teaming_types?: string,
}


/**
 * The Generative AI Profile as a whole, a cross-sectoral profile of the AI RMF and a companion resource to it.
 */
export interface GaiProfile extends AiRmfProfile {
    /** The 12 risks of section 2. */
    gai_risks: GaiRisk[],
    /** The tables of section 3, in the publication's order. */
    gai_subcategories: GaiSubcategory[],
    /** The four primary considerations of Appendix A. */
    gai_primary_considerations?: GaiPrimaryConsideration[],
}



