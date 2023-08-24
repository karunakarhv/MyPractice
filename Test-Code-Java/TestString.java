import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class TestString{
    public static void main(String[] args) {
        final String regex = "^(\\d{3}(-?)\\d{3})$";
        final String string = "123=456";
        String printStr = "test";

        final Pattern pattern = Pattern.compile(regex);
        final Matcher matcher = pattern.matcher(string);

        if (matcher.find()) {
            printStr = string.replace("-", "");
            System.out.println(printStr);
        }
        System.out.println(printStr);
    }
}