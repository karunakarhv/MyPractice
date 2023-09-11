---
title: "Basic File I/O in Java"
datePublished: Sat Sep 09 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clmcmpx7i000608mo1h8ygteu
slug: basic-file-io-in-java
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1694265493963/aead836e-f908-4d51-b633-9747db8f1446.png
tags: java, java-beginner

---

Basic file input/output (I/O) in Java allows you to read data from files and write data to files. This is a fundamental operation for reading configuration files, processing data, and saving results. Here's a step-by-step guide to performing basic file I/O in Java:

**1\. Import the Necessary Classes:**

You'll need to import classes from the [`java.io`](http://java.io) package to work with file I/O.

```java
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
```

**2\. Reading from a File:**

To read data from a file, follow these steps:

* Create a `File` object that represents the file you want to read.
    
* Create a `FileReader` to open the file for reading.
    
* Use a `BufferedReader` for efficient reading.
    
* Read data from the file line by line or character by character.
    
* Close the `FileReader` and `BufferedReader` when you're done.
    

Here's an example of reading a text file:

```java
try {
    File file = new File("example.txt"); // Replace with the path to your file
    FileReader fileReader = new FileReader(file);
    BufferedReader bufferedReader = new BufferedReader(fileReader);

    String line;
    while ((line = bufferedReader.readLine()) != null) {
        System.out.println(line); // Process each line
    }

    bufferedReader.close();
} catch (IOException e) {
    e.printStackTrace();
}
```

**3\. Writing to a File:**

To write data to a file, follow these steps:

* Create a `File` object that represents the file you want to write to.
    
* Create a `FileWriter` to open the file for writing.
    
* Use a `BufferedWriter` for efficient writing.
    
* Write data to the file.
    
* Close the `FileWriter` and `BufferedWriter` when you're done.
    

Here's an example of writing data to a text file:

```java
try {
    File file = new File("output.txt"); // Replace with the path to your file
    FileWriter fileWriter = new FileWriter(file);
    BufferedWriter bufferedWriter = new BufferedWriter(fileWriter);

    String data = "Hello, world!";
    bufferedWriter.write(data);
    
    // You can write more data or newlines as needed
    
    bufferedWriter.close();
} catch (IOException e) {
    e.printStackTrace();
}
```

**4\. Handling Exceptions:**

File I/O operations can throw `IOException`, so it's essential to handle exceptions appropriately. In the examples above, we used try-catch blocks to catch and handle any exceptions that may occur during file I/O.

**5\. Working with Binary Files:**

The examples above demonstrate how to read and write text files. If you need to work with binary files (e.g., images, audio, video), you can use `FileInputStream` and `FileOutputStream` for binary input/output.

Remember to replace `"example.txt"` and `"output.txt"` with the actual file paths you want to work with. Additionally, always close the file readers and writers using `close()` to release system resources properly.

Basic file I/O is essential for a wide range of applications, from reading configuration files to processing data from external sources.