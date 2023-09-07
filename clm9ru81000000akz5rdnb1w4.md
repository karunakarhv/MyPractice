---
title: "Structural Design Patterns in Python: Crafting Flexible and Efficient Code Structures"
datePublished: Thu Sep 07 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clm9ru81000000akz5rdnb1w4
slug: structural-design-patterns-in-python-crafting-flexible-and-efficient-code-structures
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1694077447235/0b7c72ce-a6b1-42bb-9e6c-9be519ca3ba2.jpeg
tags: python, python-beginner

---

Structural design patterns are a category of design patterns that focus on composing objects and classes into larger structures, while keeping the system flexible and efficient. These patterns help define how objects can be connected to form more complex structures, enhancing code maintainability and extensibility.

Here are some key structural design patterns commonly used in Python:

1. **Adapter Pattern:**
    
    * **Problem:** When the interface of an existing class doesn't match what is needed.
        
    * **Solution:** Create a new class (the adapter) that provides the needed interface while internally using the existing class.
        
2. **Decorator Pattern:**
    
    * **Problem:** Dynamically add responsibilities to objects without altering their code.
        
    * **Solution:** Create a set of decorator classes that are used to wrap concrete components. Decorators can add behavior before or after method calls.
        
3. **Composite Pattern:**
    
    * **Problem:** Compose objects into tree structures to represent part-whole hierarchies.
        
    * **Solution:** Create a class hierarchy where individual objects and compositions of objects share a common interface. Clients can treat individual objects and compositions uniformly.
        
4. **Proxy Pattern:**
    
    * **Problem:** Control access to an object by introducing an intermediary (proxy) with the same interface.
        
    * **Solution:** Create a proxy class that controls access to the real object, allowing for additional logic, such as lazy initialization or access control.
        
5. **Bridge Pattern:**
    
    * **Problem:** Separating an object's abstraction from its implementation, allowing both to evolve independently.
        
    * **Solution:** Use an abstraction class that delegates implementation details to a separate implementation class hierarchy.
        
6. **Facade Pattern:**
    
    * **Problem:** Provide a unified interface to a set of interfaces in a subsystem.
        
    * **Solution:** Create a facade class that provides a simplified interface to a complex system of classes, making it easier to use.
        
7. **Flyweight Pattern:**
    
    * **Problem:** Efficiently share objects to minimize memory usage or computational expense.
        
    * **Solution:** Divide the objects into intrinsic (shared) and extrinsic (context-dependent) parts. Share intrinsic parts among multiple objects.
        

**Example Usage - Adapter Pattern:**

```python
class LegacyRectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

class RectangleAdapter:
    def __init__(self, legacy_rectangle):
        self._legacy_rectangle = legacy_rectangle

    def width(self):
        return self._legacy_rectangle.get_width()

    def height(self):
        return self._legacy_rectangle.get_height()

# Usage
legacy_rect = LegacyRectangle(10, 5)
adapter = RectangleAdapter(legacy_rect)
print(f"Area: {adapter.width() * adapter.height()}")
```

**Why It Matters:**

Structural design patterns help you create flexible, maintainable, and efficient code structures by defining how objects interact and are composed. By applying these patterns, you can design software systems that are more modular, easier to extend, and less prone to tight coupling between components, making your Python codebase more robust and adaptable.