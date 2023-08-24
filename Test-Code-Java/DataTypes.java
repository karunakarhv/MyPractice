public class DataTypes {

    public static void main(String[] args) {

        //Primitive Data Types
        int i = 1234567890; //int --> integer
        float f = 1.12f; //Declaration and Initialization of primitive variables.
        long l = 1234567890133l;
        double d = 1.222222222222222;
        boolean b = false; //true or false
        char c = 'a'; //single character
        String s = "This is a Java tutorial"; //Class in Java
        // Non-Primitive variables
        DataTypes dataTypes;
        //Java is a case sensitive language.
        //Camel case - Coding Standards.

        int batmanbegins; // Less readability

        int batmanBegins; //More readability

        var testValue = Boolean.TRUE;
        if(Boolean.TRUE.equals(testValue)){
            System.out.println("True");
        }
        else{
            System.out.println("False");
        }
    }
}