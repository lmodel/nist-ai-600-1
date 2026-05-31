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
  Root container that bundles the NIST AI 600-1 Generative AI
Profile: GAI risks (Section 2), suggested actions (Section 3),
and primary considerations (Appendix A). The GAI Profile is a
*cross-sectoral* AI RMF profile (Section 1).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiProfile extends NamedThing {

  private List<GaiRisk> gaiRiskCatalog;
  private List<SuggestedAction> suggestedActions;
  private List<PrimaryGaiConsideration> primaryConsiderations;
  private List<StructuredPublicFeedback> structuredFeedbackMethods;


}