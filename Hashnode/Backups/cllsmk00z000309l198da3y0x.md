---
title: "Operators"
datePublished: Sat Aug 26 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: cllsmk00z000309l198da3y0x
slug: operators
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1692967148615/18f00d0b-7d28-4e63-a8e9-bb4c8039991c.png
tags: java, java-beginner

---

Operators in Java are symbols that perform operations on one or more operands (variables, values, expressions) to produce a result. Java provides a wide range of operators for various purposes, including arithmetic calculations, comparisons, logical operations, and more. Let's explore the main categories of operators in Java:

**1\. Arithmetic Operators:** Arithmetic operators perform basic mathematical calculations.

* `+`: Addition
    
* `-`: Subtraction
    
* `*`: Multiplication
    
* `/`: Division
    
* `%`: Modulus (remainder of division)
    

Example:

```java
int a = 10, b = 3;
int sum = a + b;        // 13
int difference = a - b; // 7
int product = a * b;    // 30
int quotient = a / b;   // 3
int remainder = a % b;  // 1
```

**2\. Comparison Operators:** Comparison operators compare two values or expressions and return a boolean result (`true` or `false`).

* `==`: Equal to
    
* `!=`: Not equal to
    
* `>`: Greater than
    
* `<`: Less than
    
* `>=`: Greater than or equal to
    
* `<=`: Less than or equal to
    

Example:

```java
int x = 5, y = 8;
boolean isEqual = x == y; // false
boolean isGreater = x > y; // false
boolean isLessThanOrEqual = x <= y; // true
```

**3\. Logical Operators:** Logical operators are used to perform logical operations on boolean values.

* `&&`: Logical AND
    
* `||`: Logical OR
    
* `!`: Logical NOT
    

Example:

```java
boolean isTrue = true, isFalse = false;
boolean resultAND = isTrue && isFalse; // false
boolean resultOR = isTrue || isFalse;  // true
boolean resultNOT = !isTrue;           // false
```

**4\. Assignment Operators:** Assignment operators are used to assign values to variables.

* `=`: Simple assignment
    
* `+=`: Addition assignment
    
* `-=`: Subtraction assignment
    
* `*=`: Multiplication assignment
    
* `/=`: Division assignment
    
* `%=`: Modulus assignment
    

Example:

```java
int num = 5;
num += 3; // num = num + 3; // 8
num *= 2; // num = num * 2; // 16
```

**5\. Increment and Decrement Operators:** Increment and decrement operators are used to increase or decrease the value of a variable by 1.

* `++`: Increment
    
* `--`: Decrement
    

Example:

```java
int count = 10;
count++; // count = count + 1; // 11
count--; // count = count - 1; // 10
```

These are some of the essential operators in Java. Understanding how to use these operators effectively is crucial for performing calculations, making comparisons, and controlling the flow of your Java programs.