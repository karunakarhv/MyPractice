---
title: "Java Object-Oriented Programming (OOP) Basics(Enapsulation): A Comprehensive Guide"
datePublished: Wed Aug 30 2023 23:00:14 GMT+0000 (Coordinated Universal Time)
cuid: cllycbge2000409jj2kyv67mj
slug: java-object-oriented-programming-oop-basicsenapsulation-a-comprehensive-guide
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1693222192524/f2bed30e-56e8-4c41-b0df-eb703d59fea2.png
tags: java, java-beginner

---

Encapsulation is one of the core principles of Object-Oriented Programming (OOP) that focuses on bundling data (attributes) and methods (functions) that operate on that data into a single unit called a class. It also involves controlling the access to the data by using access modifiers. Encapsulation helps to hide the internal details of an object and provides a well-defined interface for interacting with the object's data.

**Example of Encapsulation:**

Let's consider a simple example of encapsulation using a `Person` class:

```java
public class Person {
    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String newName) {
        if (newName != null && !newName.isEmpty()) {
            name = newName;
        }
    }

    public int getAge() {
        return age;
    }

    public void setAge(int newAge) {
        if (newAge >= 0) {
            age = newAge;
        }
    }
}
```

In this `Person` class:

* The `name` and `age` attributes are declared as `private`. This makes them inaccessible directly from outside the class.
    
* Public methods like `getName()` and `setName(String newName)` provide controlled access to the `name` attribute. Similarly, methods like `getAge()` and `setAge(int newAge)` provide controlled access to the `age` attribute.
    
* The `setName` and `setAge` methods have conditions to ensure that only valid data is assigned.
    

**Usage of Encapsulation:**

```java
public class Main {
    public static void main(String[] args) {
        Person person = new Person("Alice", 30);
        
        // Accessing data using methods
        System.out.println("Name: " + person.getName()); // Output: Name: Alice
        System.out.println("Age: " + person.getAge());   // Output: Age: 30
        
        // Modifying data using methods
        person.setName("Bob");
        person.setAge(-5); // Will be ignored due to the condition
        
        System.out.println("Updated Name: " + person.getName()); // Output: Updated Name: Bob
        System.out.println("Updated Age: " + person.getAge());   // Output: Updated Age: 30
    }
}
```

In this example:

* The attributes `name` and `age` are not accessible directly from outside the class due to their `private` access modifier.
    
* Access to these attributes is provided through getter and setter methods.
    
* Setter methods have conditions that control the modification of data.
    

Encapsulation ensures data integrity and enables you to enforce rules and validation before modifying attributes. It also provides a clear interface for using the class, making it easier to understand and maintain code.