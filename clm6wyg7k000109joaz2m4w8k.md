---
title: "Basic Input and Output in Java"
datePublished: Tue Sep 05 2023 23:00:09 GMT+0000 (Coordinated Universal Time)
cuid: clm6wyg7k000109joaz2m4w8k
slug: basic-input-and-output-in-java
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1693919065788/6a00d4e7-dfa4-4ded-9129-9923d34ef0e5.png
tags: java, java-beginner

---

Basic Input and Output (I/O) operations are fundamental in programming as they allow you to communicate with users, read data from external sources, and display results. In Java, these operations are primarily handled using the [`java.io`](http://java.io) package and the `System` class. Let's explore basic input and output in Java:

**1\. Output (Printing to the Console):**

You can use `System.out.println()` or `System.out.print()` to display output to the console:

```java
System.out.println("Hello, World!"); // Adds a new line after printing
System.out.print("Java is ");
System.out.print("awesome!"); // No new line
```

**2\. Input (Reading from the Console):**

To read input from the console, you can use the `Scanner` class from the `java.util` package:

```java
import java.util.Scanner;

public class InputExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your name: ");
        String name = scanner.nextLine(); // Read a whole line of text
        System.out.println("Hello, " + name);

        System.out.print("Enter your age: ");
        int age = scanner.nextInt(); // Read an integer
        System.out.println("You are " + age + " years old.");

        scanner.close(); // Close the scanner when done
    }
}
```

**3\. File Input and Output:**

To read from and write to files, you can use classes like `FileInputStream`, `FileOutputStream`, `FileReader`, `FileWriter`, and more from the [`java.io`](http://java.io) package. Here's a basic example of reading from a file:

```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FileInputExample {
    public static void main(String[] args) {
        try {
            FileReader fileReader = new FileReader("example.txt");
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
            }
            
            bufferedReader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

**4\. Output Formatting:**

You can use formatting options to control the appearance of output using `printf()` method:

```java
String name = "Alice";
int age = 30;

System.out.printf("Name: %s, Age: %d%n", name, age);
```

**5\. Error Output:**

Error messages can be displayed using `System.err`:

```java
System.err.println("This is an error message.");
```

**6\. Reading Command-Line Arguments:**

You can access command-line arguments passed to your Java program via the `args` parameter in the `main` method:

```java
public class CommandLineArgs {
    public static void main(String[] args) {
        System.out.println("Number of arguments: " + args.length);
        for (String arg : args) {
            System.out.println("Argument: " + arg);
        }
    }
}
```

These are the basic input and output operations in Java. Depending on your specific needs, you can explore more advanced I/O options and libraries for working with files, databases, and network communication.