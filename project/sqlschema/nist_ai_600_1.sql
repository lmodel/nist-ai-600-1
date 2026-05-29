-- # Abstract Class: NamedThing Description: Abstract base for identifiable elements of the GAI Profile.Inlined here to keep this schema standalone; mirrors the`NamedThing` defined in NIST AI 100-1.
--     * Slot: id Description: Unique identifier for an element.
--     * Slot: title Description: Human-readable title.
--     * Slot: description Description: Free-text description.
-- # Class: GaiRisk Description: A risk that is novel to or exacerbated by Generative AI.Each instance corresponds to one of the 12 risk categoriesenumerated in NIST AI 600-1 Section 2.
--     * Slot: gai_risk_kind Description: The GAI risk category this element represents.
--     * Slot: risk_categorization Description: Higher-level categorisation - technical/model, misuse, orecosystem/societal.
--     * Slot: id Description: Unique identifier for an element.
--     * Slot: title Description: Human-readable title.
--     * Slot: description Description: Free-text description.
--     * Slot: GaiProfile_id Description: Autocreated FK slot
-- # Class: SuggestedAction Description: A suggested action an organisation can take to manage GAIrisks. Each action is identified by an Action ID, linked to anAI RMF subcategory, and may be relevant to one or more GAIrisks and AI actor tasks (NIST AI 600-1 Section 3).
--     * Slot: action_id Description: Identifier of a Suggested Action.
--     * Slot: function_prefix Description: Two-letter function prefix of the action's subcategory.
--     * Slot: applies_to_subcategory Description: Identifier of the AI RMF subcategory the action applies to.
--     * Slot: id Description: Identifier for the action - typically the same as the`action_id` (e.g., "GV-1.1-001").
--     * Slot: title Description: Human-readable title.
--     * Slot: description Description: The suggested-action text itself.
--     * Slot: GaiProfile_id Description: Autocreated FK slot
-- # Class: PrimaryGaiConsideration Description: An overarching consideration derived from the NIST GAI PWGconsultation process (Appendix A). The `consideration_kind`attribute discriminates between the four primaryconsiderations: Governance, Pre-Deployment Testing, ContentProvenance, and Incident Disclosure.All consideration-specific attributes are optional and applyto the appropriate `consideration_kind`:  * GOVERNANCE: governance_practices, third_party_considerations  * PRE_DEPLOYMENT_TESTING: limitations_of_current_approaches  * CONTENT_PROVENANCE: provenance_techniques  * INCIDENT_DISCLOSURE: ai_incident_definition
--     * Slot: consideration_kind Description: Which primary consideration this element represents.
--     * Slot: third_party_considerations Description: Considerations for third-party GAI integrations, procurement,SBOMs, SLAs, and SSAE reports (Appendix A.1.3).
--     * Slot: limitations_of_current_approaches Description: For Pre-Deployment Testing: free-text discussion of whycurrent TEVV approaches may be inadequate (Appendix A.1.4).
--     * Slot: ai_incident_definition Description: For Incident Disclosure: the definition of AI incident usedby the organisation (Appendix A.1.8).
--     * Slot: id Description: Unique identifier for an element.
--     * Slot: title Description: Human-readable title.
--     * Slot: description Description: Free-text description.
--     * Slot: GaiProfile_id Description: Autocreated FK slot
-- # Class: StructuredPublicFeedback Description: Methods used to evaluate whether GAI systems are performing asintended and to calibrate and verify traditional measurementmethods (A.1.5).
--     * Slot: feedback_method_kind Description: Which structured feedback method this element represents.
--     * Slot: id Description: Unique identifier for an element.
--     * Slot: title Description: Human-readable title.
--     * Slot: description Description: Free-text description.
--     * Slot: GaiProfile_id Description: Autocreated FK slot
-- # Class: AiRedTeaming Description: A structured testing exercise used to probe an AI system tofind flaws and vulnerabilities such as inaccurate, harmful, ordiscriminatory outputs, often in a controlled environment andin collaboration with system developers (A.1.5).
--     * Slot: red_team_type Description: The type of AI red-teaming exercise.
--     * Slot: feedback_method_kind Description: Which structured feedback method this element represents.
--     * Slot: id Description: Unique identifier for an element.
--     * Slot: title Description: Human-readable title.
--     * Slot: description Description: Free-text description.
-- # Class: GaiProfile Description: Root container that bundles the NIST AI 600-1 Generative AIProfile: GAI risks (Section 2), suggested actions (Section 3),and primary considerations (Appendix A). The GAI Profile is a*cross-sectoral* AI RMF profile (Section 1).
--     * Slot: id Description: Unique identifier for an element.
--     * Slot: title Description: Human-readable title.
--     * Slot: description Description: Free-text description.
-- # Class: GaiRisk_risk_scope
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: risk_scope Description: Scope levels at which the risk may manifest.
-- # Class: GaiRisk_risk_sources
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: risk_sources Description: Sources from which the risk may emerge.
-- # Class: GaiRisk_time_scale
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: time_scale Description: Time scales over which the risk may materialise.
-- # Class: GaiRisk_lifecycle_stage
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: lifecycle_stage Description: AI lifecycle stage(s) at which a GAI risk may arise or atwhich a suggested action applies (Section 2).
-- # Class: GaiRisk_trustworthiness_characteristic
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: trustworthiness_characteristic Description: Trustworthy AI Characteristic(s) most relevant to a GAI risk -i.e., the "Trustworthy AI Characteristics" tag at the end ofeach Section 2 risk description.
-- # Class: GaiRisk_addressed_by_actions
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: addressed_by_actions_id Description: Suggested actions that address a GAI risk (back-referencederived from `SuggestedAction.gai_risks`).
-- # Class: SuggestedAction_gai_risks
--     * Slot: SuggestedAction_id Description: Autocreated FK slot
--     * Slot: gai_risks Description: GAI risk categories addressed by a suggested action orconsidered by a primary consideration.
-- # Class: SuggestedAction_actor_task
--     * Slot: SuggestedAction_id Description: Autocreated FK slot
--     * Slot: actor_task Description: Pertinent AI Actor Task(s) for a suggested action - i.e., the"AI Actor Tasks" row at the bottom of each Section 3 table.
-- # Class: PrimaryGaiConsideration_governance_practices
--     * Slot: PrimaryGaiConsideration_id Description: Autocreated FK slot
--     * Slot: governance_practices Description: Governance plans and actions enumerated in NIST AI 600-1Appendix A.1.2 (Organizational Governance).
-- # Class: PrimaryGaiConsideration_provenance_techniques
--     * Slot: PrimaryGaiConsideration_id Description: Autocreated FK slot
--     * Slot: provenance_techniques Description: For Content Provenance: provenance data tracking techniquessuch as digital watermarking, metadata recording, digitalfingerprinting, and human authentication (Appendix A.1.6).

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NamedThing_id" ON "NamedThing" (id);

CREATE TABLE "AiRedTeaming" (
	red_team_type VARCHAR(14),
	feedback_method_kind VARCHAR(32) NOT NULL,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AiRedTeaming_id" ON "AiRedTeaming" (id);

CREATE TABLE "GaiProfile" (
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiProfile_id" ON "GaiProfile" (id);

CREATE TABLE "GaiRisk" (
	gai_risk_kind VARCHAR(37),
	risk_categorization VARCHAR(27),
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"GaiProfile_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_id") REFERENCES "GaiProfile" (id)
);
CREATE INDEX "ix_GaiRisk_id" ON "GaiRisk" (id);

CREATE TABLE "SuggestedAction" (
	action_id TEXT NOT NULL,
	function_prefix VARCHAR(2),
	applies_to_subcategory TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"GaiProfile_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_id") REFERENCES "GaiProfile" (id)
);
CREATE INDEX "ix_SuggestedAction_id" ON "SuggestedAction" (id);

CREATE TABLE "PrimaryGaiConsideration" (
	consideration_kind VARCHAR(22) NOT NULL,
	third_party_considerations TEXT,
	limitations_of_current_approaches TEXT,
	ai_incident_definition TEXT,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"GaiProfile_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_id") REFERENCES "GaiProfile" (id)
);
CREATE INDEX "ix_PrimaryGaiConsideration_id" ON "PrimaryGaiConsideration" (id);

CREATE TABLE "StructuredPublicFeedback" (
	feedback_method_kind VARCHAR(32) NOT NULL,
	id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"GaiProfile_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_id") REFERENCES "GaiProfile" (id)
);
CREATE INDEX "ix_StructuredPublicFeedback_id" ON "StructuredPublicFeedback" (id);

CREATE TABLE "GaiRisk_risk_scope" (
	"GaiRisk_id" TEXT,
	risk_scope VARCHAR(29),
	PRIMARY KEY ("GaiRisk_id", risk_scope),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_risk_scope_GaiRisk_id" ON "GaiRisk_risk_scope" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_risk_scope_risk_scope" ON "GaiRisk_risk_scope" (risk_scope);

CREATE TABLE "GaiRisk_risk_sources" (
	"GaiRisk_id" TEXT,
	risk_sources VARCHAR(20),
	PRIMARY KEY ("GaiRisk_id", risk_sources),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_risk_sources_risk_sources" ON "GaiRisk_risk_sources" (risk_sources);
CREATE INDEX "ix_GaiRisk_risk_sources_GaiRisk_id" ON "GaiRisk_risk_sources" ("GaiRisk_id");

CREATE TABLE "GaiRisk_time_scale" (
	"GaiRisk_id" TEXT,
	time_scale VARCHAR(9),
	PRIMARY KEY ("GaiRisk_id", time_scale),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_time_scale_GaiRisk_id" ON "GaiRisk_time_scale" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_time_scale_time_scale" ON "GaiRisk_time_scale" (time_scale);

CREATE TABLE "GaiRisk_lifecycle_stage" (
	"GaiRisk_id" TEXT,
	lifecycle_stage VARCHAR(15),
	PRIMARY KEY ("GaiRisk_id", lifecycle_stage),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_lifecycle_stage_GaiRisk_id" ON "GaiRisk_lifecycle_stage" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_lifecycle_stage_lifecycle_stage" ON "GaiRisk_lifecycle_stage" (lifecycle_stage);

CREATE TABLE "GaiRisk_trustworthiness_characteristic" (
	"GaiRisk_id" TEXT,
	trustworthiness_characteristic VARCHAR(30),
	PRIMARY KEY ("GaiRisk_id", trustworthiness_characteristic),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_trustworthiness_characteristic_trustworthiness_characteristic" ON "GaiRisk_trustworthiness_characteristic" (trustworthiness_characteristic);
CREATE INDEX "ix_GaiRisk_trustworthiness_characteristic_GaiRisk_id" ON "GaiRisk_trustworthiness_characteristic" ("GaiRisk_id");

CREATE TABLE "GaiRisk_addressed_by_actions" (
	"GaiRisk_id" TEXT,
	addressed_by_actions_id TEXT,
	PRIMARY KEY ("GaiRisk_id", addressed_by_actions_id),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id),
	FOREIGN KEY(addressed_by_actions_id) REFERENCES "SuggestedAction" (id)
);
CREATE INDEX "ix_GaiRisk_addressed_by_actions_addressed_by_actions_id" ON "GaiRisk_addressed_by_actions" (addressed_by_actions_id);
CREATE INDEX "ix_GaiRisk_addressed_by_actions_GaiRisk_id" ON "GaiRisk_addressed_by_actions" ("GaiRisk_id");

CREATE TABLE "SuggestedAction_gai_risks" (
	"SuggestedAction_id" TEXT,
	gai_risks VARCHAR(37),
	PRIMARY KEY ("SuggestedAction_id", gai_risks),
	FOREIGN KEY("SuggestedAction_id") REFERENCES "SuggestedAction" (id)
);
CREATE INDEX "ix_SuggestedAction_gai_risks_gai_risks" ON "SuggestedAction_gai_risks" (gai_risks);
CREATE INDEX "ix_SuggestedAction_gai_risks_SuggestedAction_id" ON "SuggestedAction_gai_risks" ("SuggestedAction_id");

CREATE TABLE "SuggestedAction_actor_task" (
	"SuggestedAction_id" TEXT,
	actor_task VARCHAR(36),
	PRIMARY KEY ("SuggestedAction_id", actor_task),
	FOREIGN KEY("SuggestedAction_id") REFERENCES "SuggestedAction" (id)
);
CREATE INDEX "ix_SuggestedAction_actor_task_actor_task" ON "SuggestedAction_actor_task" (actor_task);
CREATE INDEX "ix_SuggestedAction_actor_task_SuggestedAction_id" ON "SuggestedAction_actor_task" ("SuggestedAction_id");

CREATE TABLE "PrimaryGaiConsideration_governance_practices" (
	"PrimaryGaiConsideration_id" TEXT,
	governance_practices VARCHAR(47),
	PRIMARY KEY ("PrimaryGaiConsideration_id", governance_practices),
	FOREIGN KEY("PrimaryGaiConsideration_id") REFERENCES "PrimaryGaiConsideration" (id)
);
CREATE INDEX "ix_PrimaryGaiConsideration_governance_practices_PrimaryGaiConsideration_id" ON "PrimaryGaiConsideration_governance_practices" ("PrimaryGaiConsideration_id");
CREATE INDEX "ix_PrimaryGaiConsideration_governance_practices_governance_practices" ON "PrimaryGaiConsideration_governance_practices" (governance_practices);

CREATE TABLE "PrimaryGaiConsideration_provenance_techniques" (
	"PrimaryGaiConsideration_id" TEXT,
	provenance_techniques VARCHAR(22),
	PRIMARY KEY ("PrimaryGaiConsideration_id", provenance_techniques),
	FOREIGN KEY("PrimaryGaiConsideration_id") REFERENCES "PrimaryGaiConsideration" (id)
);
CREATE INDEX "ix_PrimaryGaiConsideration_provenance_techniques_provenance_techniques" ON "PrimaryGaiConsideration_provenance_techniques" (provenance_techniques);
CREATE INDEX "ix_PrimaryGaiConsideration_provenance_techniques_PrimaryGaiConsideration_id" ON "PrimaryGaiConsideration_provenance_techniques" ("PrimaryGaiConsideration_id");
