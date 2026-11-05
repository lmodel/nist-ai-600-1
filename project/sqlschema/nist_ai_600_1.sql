-- # Class: GaiProfile Description: The Generative AI Profile as a whole, a cross-sectoral profile of the AI RMF and a companion resource to it.
--     * Slot: ai_rmf_profile_setting Description: The sector, industry, technology, organization or end use the profile covers, such as hiring.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Abstract Class: AiRmfRecord Description: The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct from what the publication itself lists.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfProfile Description: An implementation of the Core's functions, categories and subcategories for a setting, application or technology, based on the adopter's requirements, risk tolerance and resources.
--     * Slot: ai_rmf_profile_setting Description: The sector, industry, technology, organization or end use the profile covers, such as hiring.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiRisk Description: A risk that section 2 defines as unique to or made worse by the development and use of GAI.
--     * Slot: id
--     * Slot: description Description: The risk's definition in section 2.
--     * Slot: gai_risk_name Description: Which of the 12 risks this is.
--     * Slot: gai_risk_section Description: The subsection of section 2 that discusses the risk, such as 2.1.
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
-- # Class: GaiSubcategory Description: An AI RMF subcategory as one table of section 3 addresses it. The Profile covers only some of the 72.
--     * Slot: id
--     * Slot: ai_rmf_subcategory_id Description: The subcategory's identifier, such as GOVERN 1.1.
--     * Slot: description Description: The subcategory's statement as the table restates it.
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
-- # Class: GaiSuggestedAction Description: A step an organization or AI actor can take to manage GAI risks, which one row of a table states.
--     * Slot: id
--     * Slot: gai_action_id Description: The action's identifier, such as GV-1.1-001.
--     * Slot: description Description: The action's text in the table.
--     * Slot: GaiSubcategory_id Description: Autocreated FK slot
-- # Abstract Class: GaiPrimaryConsideration Description: One of the four primary considerations of Appendix A, which also inform the suggested actions.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
-- # Class: GaiGovernanceConsideration Description: How an organization's governance can be revisited for GAI, including across the AI value chain.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiPreDeploymentTestingConsideration Description: How GAI can be tested before deployment while better approaches mature, and where current tests fall short.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiContentProvenanceConsideration Description: How tracking the origin and history of content helps tell authentic content from synthetic content.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiIncidentDisclosureConsideration Description: How documenting, reporting and sharing AI incidents helps prevent harm, though no formal channels exist.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Abstract Class: GaiStructuredFeedback Description: A way of using structured public feedback to evaluate whether GAI systems perform as intended.
--     * Slot: id
--     * Slot: gai_feedback_type Description: Which of the three classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: GaiPreDeploymentTestingConsideration_id Description: Autocreated FK slot
-- # Class: GaiParticipatoryEngagement Description: Asking civil society groups, affected communities and users for feedback, such as through focus groups or surveys.
--     * Slot: id
--     * Slot: gai_feedback_type Description: Which of the three classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiFieldTesting Description: Structured settings that show how people interact with and use AI-generated information.
--     * Slot: id
--     * Slot: gai_feedback_type Description: Which of the three classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiAiRedTeaming Description: A structured exercise that probes an AI system for flaws and vulnerabilities, often with its developers.
--     * Slot: id
--     * Slot: gai_feedback_type Description: Which of the three classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiProfile_ai_rmf_profile_kinds
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_kinds Description: Which of the publication's kinds of profile this is. A current profile for one use case is both.
-- # Class: GaiProfile_ai_rmf_profile_subcategories
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_subcategories Description: The subcategories the profile selects. An adopter may select from them rather than apply all.
-- # Class: AiRmfProfile_ai_rmf_profile_kinds
--     * Slot: AiRmfProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_kinds Description: Which of the publication's kinds of profile this is. A current profile for one use case is both.
-- # Class: AiRmfProfile_ai_rmf_profile_subcategories
--     * Slot: AiRmfProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_subcategories Description: The subcategories the profile selects. An adopter may select from them rather than apply all.
-- # Class: GaiRisk_gai_risk_characteristics
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_characteristics Description: The AI RMF's trustworthiness characteristics that the subsection names for the risk.
-- # Class: GaiRisk_gai_risk_groupings
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_groupings Description: The groups footnote 5 suggests for the risk. The footnote lists Data Privacy under all three.
-- # Class: GaiRisk_gai_risk_lifecycle_stages
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_lifecycle_stages Description: The lifecycle stages where the risk can arise for the adopter's model, system or use case.
-- # Class: GaiRisk_gai_risk_scopes
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_scopes Description: The levels where the risk exists for the adopter's model, system or use case.
-- # Class: GaiRisk_gai_risk_sources
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_sources Description: Where the risk comes from for the adopter's model, system or use case.
-- # Class: GaiRisk_gai_risk_time_scales
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_time_scales Description: How the risk materializes over time for the adopter's model, system or use case.
-- # Class: GaiSubcategory_gai_subcategory_actor_tasks
--     * Slot: GaiSubcategory_id Description: Autocreated FK slot
--     * Slot: gai_subcategory_actor_tasks Description: The AI actor tasks the table names. They belong to the table and not to one action: the publication says not every task applies to every action.
-- # Class: GaiSuggestedAction_gai_action_risks
--     * Slot: GaiSuggestedAction_id Description: Autocreated FK slot
--     * Slot: gai_action_risks Description: The GAI risks the row tags the action with.
-- # Class: GaiPrimaryConsideration_gai_consideration_sections
--     * Slot: GaiPrimaryConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiGovernanceConsideration_gai_governance_plans
--     * Slot: GaiGovernanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_governance_plans Description: The plans and actions that section A.1.2 lists from other AI governance.
-- # Class: GaiGovernanceConsideration_gai_third_party_controls
--     * Slot: GaiGovernanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_third_party_controls Description: The existing controls that section A.1.3 says can apply to third-party GAI.
-- # Class: GaiGovernanceConsideration_gai_consideration_sections
--     * Slot: GaiGovernanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiPreDeploymentTestingConsideration_gai_consideration_sections
--     * Slot: GaiPreDeploymentTestingConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiContentProvenanceConsideration_gai_provenance_techniques
--     * Slot: GaiContentProvenanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_provenance_techniques Description: The well-known techniques for provenance data tracking that section A.1.6 names.
-- # Class: GaiContentProvenanceConsideration_gai_consideration_sections
--     * Slot: GaiContentProvenanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiIncidentDisclosureConsideration_gai_incident_harms
--     * Slot: GaiIncidentDisclosureConsideration_id Description: Autocreated FK slot
--     * Slot: gai_incident_harms Description: The kinds of harm that section A.1.8's definition of an AI incident names.
-- # Class: GaiIncidentDisclosureConsideration_gai_consideration_sections
--     * Slot: GaiIncidentDisclosureConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiAiRedTeaming_gai_red_teaming_types
--     * Slot: GaiAiRedTeaming_id Description: Autocreated FK slot
--     * Slot: gai_red_teaming_types Description: The kinds of AI red-teaming that may suit the use case.

CREATE TABLE "GaiProfile" (
	ai_rmf_profile_setting TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_GaiProfile_ai_rmf_id" ON "GaiProfile" (ai_rmf_id);

CREATE TABLE "AiRmfRecord" (
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRecord_ai_rmf_id" ON "AiRmfRecord" (ai_rmf_id);

CREATE TABLE "AiRmfProfile" (
	ai_rmf_profile_setting TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_id" ON "AiRmfProfile" (ai_rmf_id);

CREATE TABLE "GaiGovernanceConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiGovernanceConsideration_id" ON "GaiGovernanceConsideration" (id);

CREATE TABLE "GaiPreDeploymentTestingConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiPreDeploymentTestingConsideration_id" ON "GaiPreDeploymentTestingConsideration" (id);

CREATE TABLE "GaiContentProvenanceConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiContentProvenanceConsideration_id" ON "GaiContentProvenanceConsideration" (id);

CREATE TABLE "GaiIncidentDisclosureConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_id" ON "GaiIncidentDisclosureConsideration" (id);

CREATE TABLE "GaiParticipatoryEngagement" (
	id INTEGER NOT NULL,
	gai_feedback_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiParticipatoryEngagement_id" ON "GaiParticipatoryEngagement" (id);

CREATE TABLE "GaiFieldTesting" (
	id INTEGER NOT NULL,
	gai_feedback_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiFieldTesting_id" ON "GaiFieldTesting" (id);

CREATE TABLE "GaiAiRedTeaming" (
	id INTEGER NOT NULL,
	gai_feedback_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiAiRedTeaming_id" ON "GaiAiRedTeaming" (id);

CREATE TABLE "GaiRisk" (
	id INTEGER NOT NULL,
	description TEXT,
	gai_risk_name VARCHAR(37) NOT NULL,
	gai_risk_section TEXT NOT NULL,
	"GaiProfile_ai_rmf_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiRisk_id" ON "GaiRisk" (id);

CREATE TABLE "GaiSubcategory" (
	id INTEGER NOT NULL,
	ai_rmf_subcategory_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"GaiProfile_ai_rmf_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiSubcategory_id" ON "GaiSubcategory" (id);

CREATE TABLE "GaiPrimaryConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"GaiProfile_ai_rmf_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiPrimaryConsideration_id" ON "GaiPrimaryConsideration" (id);

CREATE TABLE "GaiStructuredFeedback" (
	id INTEGER NOT NULL,
	gai_feedback_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"GaiPreDeploymentTestingConsideration_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiPreDeploymentTestingConsideration_id") REFERENCES "GaiPreDeploymentTestingConsideration" (id)
);
CREATE INDEX "ix_GaiStructuredFeedback_id" ON "GaiStructuredFeedback" (id);

CREATE TABLE "GaiProfile_ai_rmf_profile_kinds" (
	"GaiProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_kinds VARCHAR(14) NOT NULL,
	PRIMARY KEY ("GaiProfile_ai_rmf_id", ai_rmf_profile_kinds),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiProfile_ai_rmf_profile_kinds_ai_rmf_profile_kinds" ON "GaiProfile_ai_rmf_profile_kinds" (ai_rmf_profile_kinds);
CREATE INDEX "ix_GaiProfile_ai_rmf_profile_kinds_GaiProfile_ai_rmf_id" ON "GaiProfile_ai_rmf_profile_kinds" ("GaiProfile_ai_rmf_id");

CREATE TABLE "GaiProfile_ai_rmf_profile_subcategories" (
	"GaiProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_subcategories TEXT,
	PRIMARY KEY ("GaiProfile_ai_rmf_id", ai_rmf_profile_subcategories),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiProfile_ai_rmf_profile_subcategories_GaiProfile_ai_rmf_id" ON "GaiProfile_ai_rmf_profile_subcategories" ("GaiProfile_ai_rmf_id");
CREATE INDEX "ix_GaiProfile_ai_rmf_profile_subcategories_ai_rmf_profile_subcategories" ON "GaiProfile_ai_rmf_profile_subcategories" (ai_rmf_profile_subcategories);

CREATE TABLE "AiRmfProfile_ai_rmf_profile_kinds" (
	"AiRmfProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_kinds VARCHAR(14) NOT NULL,
	PRIMARY KEY ("AiRmfProfile_ai_rmf_id", ai_rmf_profile_kinds),
	FOREIGN KEY("AiRmfProfile_ai_rmf_id") REFERENCES "AiRmfProfile" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_kinds_ai_rmf_profile_kinds" ON "AiRmfProfile_ai_rmf_profile_kinds" (ai_rmf_profile_kinds);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_kinds_AiRmfProfile_ai_rmf_id" ON "AiRmfProfile_ai_rmf_profile_kinds" ("AiRmfProfile_ai_rmf_id");

CREATE TABLE "AiRmfProfile_ai_rmf_profile_subcategories" (
	"AiRmfProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_subcategories TEXT,
	PRIMARY KEY ("AiRmfProfile_ai_rmf_id", ai_rmf_profile_subcategories),
	FOREIGN KEY("AiRmfProfile_ai_rmf_id") REFERENCES "AiRmfProfile" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_subcategories_AiRmfProfile_ai_rmf_id" ON "AiRmfProfile_ai_rmf_profile_subcategories" ("AiRmfProfile_ai_rmf_id");
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_subcategories_ai_rmf_profile_subcategories" ON "AiRmfProfile_ai_rmf_profile_subcategories" (ai_rmf_profile_subcategories);

CREATE TABLE "GaiGovernanceConsideration_gai_governance_plans" (
	"GaiGovernanceConsideration_id" INTEGER,
	gai_governance_plans VARCHAR(61),
	PRIMARY KEY ("GaiGovernanceConsideration_id", gai_governance_plans),
	FOREIGN KEY("GaiGovernanceConsideration_id") REFERENCES "GaiGovernanceConsideration" (id)
);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_governance_plans_gai_governance_plans" ON "GaiGovernanceConsideration_gai_governance_plans" (gai_governance_plans);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_governance_plans_GaiGovernanceConsideration_id" ON "GaiGovernanceConsideration_gai_governance_plans" ("GaiGovernanceConsideration_id");

CREATE TABLE "GaiGovernanceConsideration_gai_third_party_controls" (
	"GaiGovernanceConsideration_id" INTEGER,
	gai_third_party_controls VARCHAR(41),
	PRIMARY KEY ("GaiGovernanceConsideration_id", gai_third_party_controls),
	FOREIGN KEY("GaiGovernanceConsideration_id") REFERENCES "GaiGovernanceConsideration" (id)
);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_third_party_controls_gai_third_party_controls" ON "GaiGovernanceConsideration_gai_third_party_controls" (gai_third_party_controls);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_third_party_controls_GaiGovernanceConsideration_id" ON "GaiGovernanceConsideration_gai_third_party_controls" ("GaiGovernanceConsideration_id");

CREATE TABLE "GaiGovernanceConsideration_gai_consideration_sections" (
	"GaiGovernanceConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiGovernanceConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiGovernanceConsideration_id") REFERENCES "GaiGovernanceConsideration" (id)
);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiGovernanceConsideration_gai_consideration_sections" (gai_consideration_sections);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_consideration_sections_GaiGovernanceConsideration_id" ON "GaiGovernanceConsideration_gai_consideration_sections" ("GaiGovernanceConsideration_id");

CREATE TABLE "GaiPreDeploymentTestingConsideration_gai_consideration_sections" (
	"GaiPreDeploymentTestingConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiPreDeploymentTestingConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiPreDeploymentTestingConsideration_id") REFERENCES "GaiPreDeploymentTestingConsideration" (id)
);
CREATE INDEX "ix_GaiPreDeploymentTestingConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiPreDeploymentTestingConsideration_gai_consideration_sections" (gai_consideration_sections);
CREATE INDEX "ix_GaiPreDeploymentTestingConsideration_gai_consideration_sections_GaiPreDeploymentTestingConsideration_id" ON "GaiPreDeploymentTestingConsideration_gai_consideration_sections" ("GaiPreDeploymentTestingConsideration_id");

CREATE TABLE "GaiContentProvenanceConsideration_gai_provenance_techniques" (
	"GaiContentProvenanceConsideration_id" INTEGER,
	gai_provenance_techniques VARCHAR(22),
	PRIMARY KEY ("GaiContentProvenanceConsideration_id", gai_provenance_techniques),
	FOREIGN KEY("GaiContentProvenanceConsideration_id") REFERENCES "GaiContentProvenanceConsideration" (id)
);
CREATE INDEX "ix_GaiContentProvenanceConsideration_gai_provenance_techniques_gai_provenance_techniques" ON "GaiContentProvenanceConsideration_gai_provenance_techniques" (gai_provenance_techniques);
CREATE INDEX "ix_GaiContentProvenanceConsideration_gai_provenance_techniques_GaiContentProvenanceConsideration_id" ON "GaiContentProvenanceConsideration_gai_provenance_techniques" ("GaiContentProvenanceConsideration_id");

CREATE TABLE "GaiContentProvenanceConsideration_gai_consideration_sections" (
	"GaiContentProvenanceConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiContentProvenanceConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiContentProvenanceConsideration_id") REFERENCES "GaiContentProvenanceConsideration" (id)
);
CREATE INDEX "ix_GaiContentProvenanceConsideration_gai_consideration_sections_GaiContentProvenanceConsideration_id" ON "GaiContentProvenanceConsideration_gai_consideration_sections" ("GaiContentProvenanceConsideration_id");
CREATE INDEX "ix_GaiContentProvenanceConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiContentProvenanceConsideration_gai_consideration_sections" (gai_consideration_sections);

CREATE TABLE "GaiIncidentDisclosureConsideration_gai_incident_harms" (
	"GaiIncidentDisclosureConsideration_id" INTEGER,
	gai_incident_harms VARCHAR(43),
	PRIMARY KEY ("GaiIncidentDisclosureConsideration_id", gai_incident_harms),
	FOREIGN KEY("GaiIncidentDisclosureConsideration_id") REFERENCES "GaiIncidentDisclosureConsideration" (id)
);
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_gai_incident_harms_GaiIncidentDisclosureConsideration_id" ON "GaiIncidentDisclosureConsideration_gai_incident_harms" ("GaiIncidentDisclosureConsideration_id");
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_gai_incident_harms_gai_incident_harms" ON "GaiIncidentDisclosureConsideration_gai_incident_harms" (gai_incident_harms);

CREATE TABLE "GaiIncidentDisclosureConsideration_gai_consideration_sections" (
	"GaiIncidentDisclosureConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiIncidentDisclosureConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiIncidentDisclosureConsideration_id") REFERENCES "GaiIncidentDisclosureConsideration" (id)
);
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_gai_consideration_sections_GaiIncidentDisclosureConsideration_id" ON "GaiIncidentDisclosureConsideration_gai_consideration_sections" ("GaiIncidentDisclosureConsideration_id");
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiIncidentDisclosureConsideration_gai_consideration_sections" (gai_consideration_sections);

CREATE TABLE "GaiAiRedTeaming_gai_red_teaming_types" (
	"GaiAiRedTeaming_id" INTEGER,
	gai_red_teaming_types VARCHAR(14),
	PRIMARY KEY ("GaiAiRedTeaming_id", gai_red_teaming_types),
	FOREIGN KEY("GaiAiRedTeaming_id") REFERENCES "GaiAiRedTeaming" (id)
);
CREATE INDEX "ix_GaiAiRedTeaming_gai_red_teaming_types_GaiAiRedTeaming_id" ON "GaiAiRedTeaming_gai_red_teaming_types" ("GaiAiRedTeaming_id");
CREATE INDEX "ix_GaiAiRedTeaming_gai_red_teaming_types_gai_red_teaming_types" ON "GaiAiRedTeaming_gai_red_teaming_types" (gai_red_teaming_types);

CREATE TABLE "GaiSuggestedAction" (
	id INTEGER NOT NULL,
	gai_action_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"GaiSubcategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiSubcategory_id") REFERENCES "GaiSubcategory" (id)
);
CREATE INDEX "ix_GaiSuggestedAction_id" ON "GaiSuggestedAction" (id);

CREATE TABLE "GaiRisk_gai_risk_characteristics" (
	"GaiRisk_id" INTEGER,
	gai_risk_characteristics VARCHAR(30),
	PRIMARY KEY ("GaiRisk_id", gai_risk_characteristics),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_characteristics_GaiRisk_id" ON "GaiRisk_gai_risk_characteristics" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_gai_risk_characteristics_gai_risk_characteristics" ON "GaiRisk_gai_risk_characteristics" (gai_risk_characteristics);

CREATE TABLE "GaiRisk_gai_risk_groupings" (
	"GaiRisk_id" INTEGER,
	gai_risk_groupings VARCHAR(21),
	PRIMARY KEY ("GaiRisk_id", gai_risk_groupings),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_groupings_gai_risk_groupings" ON "GaiRisk_gai_risk_groupings" (gai_risk_groupings);
CREATE INDEX "ix_GaiRisk_gai_risk_groupings_GaiRisk_id" ON "GaiRisk_gai_risk_groupings" ("GaiRisk_id");

CREATE TABLE "GaiRisk_gai_risk_lifecycle_stages" (
	"GaiRisk_id" INTEGER,
	gai_risk_lifecycle_stages VARCHAR(15),
	PRIMARY KEY ("GaiRisk_id", gai_risk_lifecycle_stages),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_lifecycle_stages_GaiRisk_id" ON "GaiRisk_gai_risk_lifecycle_stages" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_gai_risk_lifecycle_stages_gai_risk_lifecycle_stages" ON "GaiRisk_gai_risk_lifecycle_stages" (gai_risk_lifecycle_stages);

CREATE TABLE "GaiRisk_gai_risk_scopes" (
	"GaiRisk_id" INTEGER,
	gai_risk_scopes VARCHAR(29),
	PRIMARY KEY ("GaiRisk_id", gai_risk_scopes),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_scopes_gai_risk_scopes" ON "GaiRisk_gai_risk_scopes" (gai_risk_scopes);
CREATE INDEX "ix_GaiRisk_gai_risk_scopes_GaiRisk_id" ON "GaiRisk_gai_risk_scopes" ("GaiRisk_id");

CREATE TABLE "GaiRisk_gai_risk_sources" (
	"GaiRisk_id" INTEGER,
	gai_risk_sources VARCHAR(20),
	PRIMARY KEY ("GaiRisk_id", gai_risk_sources),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_sources_GaiRisk_id" ON "GaiRisk_gai_risk_sources" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_gai_risk_sources_gai_risk_sources" ON "GaiRisk_gai_risk_sources" (gai_risk_sources);

CREATE TABLE "GaiRisk_gai_risk_time_scales" (
	"GaiRisk_id" INTEGER,
	gai_risk_time_scales VARCHAR(8),
	PRIMARY KEY ("GaiRisk_id", gai_risk_time_scales),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_time_scales_gai_risk_time_scales" ON "GaiRisk_gai_risk_time_scales" (gai_risk_time_scales);
CREATE INDEX "ix_GaiRisk_gai_risk_time_scales_GaiRisk_id" ON "GaiRisk_gai_risk_time_scales" ("GaiRisk_id");

CREATE TABLE "GaiSubcategory_gai_subcategory_actor_tasks" (
	"GaiSubcategory_id" INTEGER,
	gai_subcategory_actor_tasks VARCHAR(36),
	PRIMARY KEY ("GaiSubcategory_id", gai_subcategory_actor_tasks),
	FOREIGN KEY("GaiSubcategory_id") REFERENCES "GaiSubcategory" (id)
);
CREATE INDEX "ix_GaiSubcategory_gai_subcategory_actor_tasks_GaiSubcategory_id" ON "GaiSubcategory_gai_subcategory_actor_tasks" ("GaiSubcategory_id");
CREATE INDEX "ix_GaiSubcategory_gai_subcategory_actor_tasks_gai_subcategory_actor_tasks" ON "GaiSubcategory_gai_subcategory_actor_tasks" (gai_subcategory_actor_tasks);

CREATE TABLE "GaiPrimaryConsideration_gai_consideration_sections" (
	"GaiPrimaryConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiPrimaryConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiPrimaryConsideration_id") REFERENCES "GaiPrimaryConsideration" (id)
);
CREATE INDEX "ix_GaiPrimaryConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiPrimaryConsideration_gai_consideration_sections" (gai_consideration_sections);
CREATE INDEX "ix_GaiPrimaryConsideration_gai_consideration_sections_GaiPrimaryConsideration_id" ON "GaiPrimaryConsideration_gai_consideration_sections" ("GaiPrimaryConsideration_id");

CREATE TABLE "GaiSuggestedAction_gai_action_risks" (
	"GaiSuggestedAction_id" INTEGER,
	gai_action_risks VARCHAR(37),
	PRIMARY KEY ("GaiSuggestedAction_id", gai_action_risks),
	FOREIGN KEY("GaiSuggestedAction_id") REFERENCES "GaiSuggestedAction" (id)
);
CREATE INDEX "ix_GaiSuggestedAction_gai_action_risks_gai_action_risks" ON "GaiSuggestedAction_gai_action_risks" (gai_action_risks);
CREATE INDEX "ix_GaiSuggestedAction_gai_action_risks_GaiSuggestedAction_id" ON "GaiSuggestedAction_gai_action_risks" ("GaiSuggestedAction_id");
