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
  Methods used to evaluate whether GAI systems are performing as
intended and to calibrate and verify traditional measurement
methods (A.1.5).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class StructuredPublicFeedback extends NamedThing {

  private String feedbackMethodKind;


}