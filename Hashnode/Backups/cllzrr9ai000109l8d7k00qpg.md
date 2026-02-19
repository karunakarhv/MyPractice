---
title: "Java Object-Oriented Programming (OOP) Basics(Access Modifiers): A Comprehensive Guide"
datePublished: Thu Aug 31 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: cllzrr9ai000109l8d7k00qpg
slug: java-object-oriented-programming-oop-basicsaccess-modifiers-a-comprehensive-guide
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1693398031807/767b1cb7-792d-49f7-8669-7f85522d3ce9.png
tags: java, java-beginner

---

Access modifiers in Java determine the visibility and accessibility of classes, attributes, methods, and constructors within different parts of a program. They play a critical role in encapsulation and controlling the level of interaction between different parts of your code. Java offers four main access modifiers:

1. `public`:
    
    * The most permissive access level.
        
    * Members marked as `public` are accessible from any class, even outside the package.
        
2. `protected`:
    
    * Members marked as `protected` are accessible within the same package and subclasses (even if they are in different packages).
        
    * Outside the package, these members are accessible only if accessed through inheritance.
        
3. `default` (no modifier):
    
    * Also known as "package-private."
        
    * Members with no explicit access modifier are accessible only within the same package.
        
4. `private`:
    
    * The most restrictive access level.
        
    * Members marked as `private` are accessible only within the same class.
        

**Usage of Access Modifiers:**

Here's an example illustrating how access modifiers work:

```java
package com.example;

public class MyClass {
    public int publicField; // Accessible from anywhere
    protected int protectedField; // Accessible within package and subclasses
    int defaultField; // Accessible within the same package
    private int privateField; // Accessible only within the same class

    public void publicMethod() {
        // Code accessible from anywhere
    }

    protected void protectedMethod() {
        // Code accessible within package and subclasses
    }

    void defaultMethod() {
        // Code accessible within the same package
    }

    private void privateMethod() {
        // Code accessible only within the same class
    }
}
```

```java
package com.example.another;

import com.example.MyClass;

public class AnotherClass extends MyClass {
    void accessProtectedField() {
        protectedField = 10; // Accessible due to inheritance
    }

    protected void accessProtectedMethod() {
        protectedMethod(); // Accessible due to inheritance
    }
}
```

```java
package com.example;

public class Main {
    public static void main(String[] args) {
        MyClass myObject = new MyClass();
        myObject.publicField = 5; // Accessible
        myObject.protectedField = 10; // Not accessible due to package difference
        myObject.defaultField = 15; // Not accessible due to package difference
        myObject.privateField = 20; // Not accessible

        myObject.publicMethod(); // Accessible
        myObject.protectedMethod(); // Not accessible due to package difference
        myObject.defaultMethod(); // Not accessible due to package difference
        myObject.privateMethod(); // Not accessible
    }
}
```

In this example:

* Members with different access modifiers demonstrate their visibility based on the context.
    
* `AnotherClass` can access `protectedField` and `protectedMethod()` due to inheritance.
    
* The `Main` class demonstrates accessing members from the `MyClass` instance based on their access modifiers.
    

Understanding and using access modifiers effectively are important for creating well-structured and secure programs, as they control the interaction between different parts of your code.