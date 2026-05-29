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
  A structured testing exercise used to probe an AI system to
find flaws and vulnerabilities such as inaccurate, harmful, or
discriminatory outputs, often in a controlled environment and
in collaboration with system developers (A.1.5).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRedTeaming extends StructuredPublicFeedback {

  private String redTeamType;


}