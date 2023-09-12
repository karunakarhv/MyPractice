---
title: "Builder Pattern in Python: Construct Complex Objects Step by Step"
datePublished: Mon Sep 11 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clmfhlm97000309jw2qxn8u5l
slug: builder-pattern-in-python-construct-complex-objects-step-by-step
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1694436677524/ec136a4b-e67a-45d5-8a11-bb76957214ef.jpeg
tags: python, python-beginner

---

The Builder Pattern is a creational design pattern that separates the construction of a complex object from its representation. It allows you to create different variations of an object while keeping the construction process consistent.

**Key Components:**

1. **Director:** This class is responsible for orchestrating the construction process. It works with a builder to build the product.
    
2. **Builder (Interface):** The abstract builder defines the steps to build the product. Concrete builders implement these steps.
    
3. **Concrete Builder:** These are implementations of the builder interface. Each concrete builder knows how to build a specific variation of the product.
    
4. **Product:** The complex object being built. It typically has multiple parts or attributes.
    

**Example Implementation:**

Here's a simplified example of the Builder Pattern in Python:

```python
from abc import ABC, abstractmethod

# Product
class Computer:
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.storage = None

# Builder interface
class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self):
        pass

    @abstractmethod
    def set_memory(self):
        pass

    @abstractmethod
    def set_storage(self):
        pass

    @abstractmethod
    def get_computer(self):
        pass

# Concrete Builders
class BasicComputerBuilder(ComputerBuilder):
    def set_cpu(self):
        self.cpu = "Basic CPU"

    def set_memory(self):
        self.memory = "4GB RAM"

    def set_storage(self):
        self.storage = "256GB SSD"

    def get_computer(self):
        computer = Computer()
        computer.cpu = self.cpu
        computer.memory = self.memory
        computer.storage = self.storage
        return computer

class HighEndComputerBuilder(ComputerBuilder):
    def set_cpu(self):
        self.cpu = "High-end CPU"

    def set_memory(self):
        self.memory = "32GB RAM"

    def set_storage(self):
        self.storage = "2TB HDD"

    def get_computer(self):
        computer = Computer()
        computer.cpu = self.cpu
        computer.memory = self.memory
        computer.storage = self.storage
        return computer

# Director
class ComputerEngineer:
    def __init__(self, builder):
        self.builder = builder

    def construct_computer(self):
        self.builder.set_cpu()
        self.builder.set_memory()
        self.builder.set_storage()

    def get_computer(self):
        return self.builder.get_computer()

# Usage
basic_builder = BasicComputerBuilder()
engineer = ComputerEngineer(basic_builder)
engineer.construct_computer()
basic_computer = engineer.get_computer()

print(basic_computer.cpu)      # Output: Basic CPU
print(basic_computer.memory)   # Output: 4GB RAM
print(basic_computer.storage)  # Output: 256GB SSD
```

In this example, we have two concrete builders (`BasicComputerBuilder` and `HighEndComputerBuilder`) that create different types of computers. The `ComputerEngineer` directs the construction process and returns the constructed `Computer` object.

**Why It Matters:**

The Builder Pattern allows you to create complex objects with multiple configuration options, making it particularly useful when dealing with large and intricate objects. It enhances code readability and maintainability by separating object construction from its representation. Builders enable you to create objects step by step, improving flexibility and enabling the creation of various product variations.