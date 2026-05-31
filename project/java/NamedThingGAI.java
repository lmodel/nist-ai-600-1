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
  Abstract base for identifiable elements of the GAI Profile.
Inlined here to keep this schema standalone; mirrors the
`NamedThingGAI` defined in NIST AI 100-1.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class NamedThingGAI  {

  private String id;
  private String title;
  private String description;


}