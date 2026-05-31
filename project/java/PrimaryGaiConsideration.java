package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
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
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class PrimaryGaiConsideration extends NamedThing {

  private String considerationKind;
  private List<String> governancePractices;
  private String thirdPartyConsiderations;
  private String limitationsOfCurrentApproaches;
  private List<String> provenanceTechniques;
  private String aiIncidentDefinition;


}