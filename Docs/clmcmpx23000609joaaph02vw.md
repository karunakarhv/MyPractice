---
title: "Factory Method Pattern in Python: Crafting Objects Creatively"
datePublished: Sat Sep 09 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clmcmpx23000609joaaph02vw
slug: factory-method-pattern-in-python-crafting-objects-creatively
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1694264790312/8abe6a7f-00ef-41ce-a3d6-69088cd2b0b9.jpeg
tags: python, python-for-beginner

---

The Factory Method pattern is a creational design pattern that provides an interface for creating objects in a super class but allows subclasses to alter the type of objects that will be created. It promotes loose coupling and flexibility in object creation.

**Key Components:**

1. **Creator (Superclass):** This is an abstract class or interface that defines the factory method, which returns an object of the Product type. It declares the factory method but provides no implementation.
    
2. **ConcreteCreator (Subclass):** Subclasses of the Creator implement the factory method. Each subclass can produce objects of a different Product type.
    
3. **Product:** This is the abstract class or interface that defines the object created by the factory method.
    
4. **ConcreteProduct:** Subclasses of Product are the actual objects created by the factory method in ConcreteCreators.
    

**Example Implementation:**

Here's a simplified example of the Factory Method pattern in Python:

```python
from abc import ABC, abstractmethod

# Product interface
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Creator interface
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Creators
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Usage
def get_pet(factory):
    pet = factory.create_animal()
    return pet

dog_factory = DogFactory()
cat_factory = CatFactory()

dog = get_pet(dog_factory)
cat = get_pet(cat_factory)

print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
```

In this example, `AnimalFactory` is the Creator interface with the factory method `create_animal()`. Concrete creators like `DogFactory` and `CatFactory` implement this method to produce specific products (`Dog` and `Cat`).

**Why It Matters:**

The Factory Method pattern provides a way to create objects without specifying their exact classes. This flexibility allows you to introduce new products (ConcreteProducts) without modifying existing client code (which relies on the Creator interface). It promotes code reusability, maintainability, and scalability by adhering to the open-closed principle—open for extension but closed for modification.