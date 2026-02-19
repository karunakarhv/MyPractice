import java.lang.invoke.WrongMethodTypeException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

class TestNull {

  public static void main(String[] args) {
    String testStr = "null";
    if (testStr instanceof String) {
      System.out.println("Test String is null");
    } else {
      System.out.println("Test String is not null");
    }
    //testOptional();
    Wombat tesWombat = new Wombat();
    tesWombat.setTemperature(123);
  }

  public void testOptional() {
    System.out.println("Test {} String {}", null, 123);
  }
}

public class Wombat {

  static final Logger logger = LoggerFactory.getLogger(Wombat.class);
  Integer t;
  Integer oldT;

  public void setTemperature(Integer temperature) {
    oldT = t;
    t = temperature;
    logger.debug("Temperature set to {}. Old temperature was {}.", t, oldT);
    if (temperature.intValue() > 50) {
      logger.info("Temperature has risen above 50 degrees.");
    }
  }
}
