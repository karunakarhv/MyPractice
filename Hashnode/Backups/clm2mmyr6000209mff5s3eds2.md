---
title: "Java Object-Oriented Programming (OOP) Basics(Polymorphism): A Comprehensive Guide"
datePublished: Sat Sep 02 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clm2mmyr6000209mff5s3eds2
slug: java-object-oriented-programming-oop-basicspolymorphism-a-comprehensive-guide
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1693568630787/1c691812-f464-4116-ad2a-7bf64ea3ab96.png
tags: java, java-beginner

---

Polymorphism is a fundamental concept in Object-Oriented Programming (OOP) that allows objects of different classes to be treated as objects of a common superclass. It enables flexibility and extensibility in your code by allowing you to write more generic and reusable code that can work with a variety of objects. In Java, polymorphism is achieved primarily through method overriding and interfaces.

There are two types of polymorphism in Java:

1. **Compile-Time Polymorphism (Static Binding):**
    
    * Also known as method overloading.
        
    * Occurs at compile time.
        
    * Involves methods with the same name in the same class but different parameters.
        
    * The correct method to be called is determined based on the method's signature (method name and parameter types).
        
    
    ```java
    class Calculator {
        int add(int a, int b) {
            return a + b;
        }
    
        double add(double a, double b) {
            return a + b;
        }
    }
    ```
    
2. **Run-Time Polymorphism (Dynamic Binding):**
    
    * Also known as method overriding.
        
    * Occurs at runtime.
        
    * Involves a subclass providing a specific implementation of a method that is already defined in its superclass.
        
    * The correct method to be called is determined dynamically at runtime based on the object's actual type.
        
    
    ```java
    class Animal {
        void makeSound() {
            System.out.println("Animal makes a sound");
        }
    }
    
    class Dog extends Animal {
        @Override
        void makeSound() {
            System.out.println("Dog barks");
        }
    }
    ```
    

**Example of Polymorphism:**

```java
class Animal {
    void makeSound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog barks");
    }
}

class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Cat meows");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myAnimal = new Animal();
        Animal myDog = new Dog();
        Animal myCat = new Cat();

        myAnimal.makeSound(); // Output: Animal makes a sound
        myDog.makeSound();    // Output: Dog barks
        myCat.makeSound();    // Output: Cat meows
    }
}
```

In this example, `Animal` is the superclass, and `Dog` and `Cat` are subclasses. We create instances of these classes and assign them to `Animal` references. At runtime, the correct `makeSound()` method is called based on the actual type of the object (run-time polymorphism).

Polymorphism enables you to write more flexible and extensible code because you can work with objects based on their common superclass or interface, regardless of their specific implementations. This promotes code reusability and simplifies the management of complex class hierarchies.