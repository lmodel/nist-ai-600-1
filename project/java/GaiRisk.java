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
  A risk that is novel to or exacerbated by Generative AI.
Each instance corresponds to one of the 12 risk categories
enumerated in NIST AI 600-1 Section 2.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiRisk extends NamedThing {

  private String gaiRiskKind;
  private String riskCategorization;
  private List<String> riskScope;
  private List<String> riskSources;
  private List<String> timeScale;
  private List<String> lifecycleStage;
  private List<String> trustworthinessCharacteristic;
  private List<SuggestedAction> addressedByActions;


}