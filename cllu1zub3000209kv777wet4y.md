---
title: "Control Structures"
datePublished: Sun Aug 27 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: cllu1zub3000209kv777wet4y
slug: control-structures
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1693051818595/2dbb8a08-4940-4998-aeb2-0fe2f3aaba70.png
tags: java, java-beginner

---

Control structures in Java are used to control the flow of execution in a program. They allow you to make decisions, repeat actions, and create structured, organized code. Java provides three main types of control structures: conditional statements, loops, and branching.

**1\. Conditional Statements:**

Conditional statements help your program make decisions based on conditions.

* **if Statement:**
    
    ```java
    if (condition) {
        // Code to execute if condition is true
    }
    ```
    
* **if-else Statement:**
    
    ```java
    if (condition) {
        // Code to execute if condition is true
    } else {
        // Code to execute if condition is false
    }
    ```
    
* **else-if Ladder:**
    
    ```java
    if (condition1) {
        // Code to execute if condition1 is true
    } else if (condition2) {
        // Code to execute if condition2 is true
    } else {
        // Code to execute if none of the conditions is true
    }
    ```
    
* **switch Statement:**
    
    ```java
    switch (expression) {
        case value1:
            // Code for case value1
            break;
        case value2:
            // Code for case value2
            break;
        // ...
        default:
            // Code for default case
    }
    ```
    

**2\. Loops:**

Loops help you repeat a block of code multiple times.

* **while Loop:**
    
    ```java
    while (condition) {
        // Code to repeat as long as condition is true
    }
    ```
    
* **do-while Loop:**
    
    ```java
    do {
        // Code to execute at least once, then repeat while condition is true
    } while (condition);
    ```
    
* **for Loop:**
    
    ```java
    for (initialization; condition; increment/decrement) {
        // Code to repeat as long as condition is true
    }
    ```
    
* **enhanced for (foreach) Loop:**
    
    ```java
    for (data_type variable : array/collection) {
        // Code to iterate through each element of the array/collection
    }
    ```
    

**3\. Branching:**

Branching allows you to jump to specific parts of your code based on conditions.

* **break Statement:** Used to exit a loop or switch statement prematurely.
    
* **continue Statement:** Used to skip the rest of the loop's current iteration and move to the next iteration.
    
* **return Statement:** Used to exit a method and optionally return a value.
    

**Example:**

Here's an example that combines these control structures to create a simple program that prints even and odd numbers between 1 and 10:

```java
public class ControlStructuresExample {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            if (i % 2 == 0) {
                System.out.println(i + " is even");
            } else {
                System.out.println(i + " is odd");
            }
        }
    }
}
```

Control structures enable you to create dynamic, responsive, and efficient programs by guiding the flow of execution based on conditions and loops.