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
  A suggested action an organisation can take to manage GAI
risks. Each action is identified by an Action ID, linked to an
AI RMF subcategory, and may be relevant to one or more GAI
risks and AI actor tasks (NIST AI 600-1 Section 3).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SuggestedAction extends NamedThingGAI {

  private String actionId;
  private String functionPrefix;
  private String appliesToSubcategory;
  private List<String> gaiRisks;
  private List<String> actorTask;


}