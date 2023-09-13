---
title: "List Interface in Java"
datePublished: Wed Sep 13 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clmichbhy000409kz6h89bq2a
slug: list-interface-in-java
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1694606969294/8436245e-d84c-4460-801b-aaf0faeb554f.png
tags: java, java-beginner

---

In Java, the `List` collection interface is part of the Java Collections Framework, and it represents an ordered collection of elements that allows duplicate values. Lists maintain the order of insertion, which means the elements are stored in the sequence they were added. The `List` interface provides methods for adding, accessing, modifying, and removing elements from the list. Here's an overview of the `List` interface and some common implementations:

**1\. List Interface (java.util.List):**

The `List` interface defines the following key methods:

* `add(E element)`: Adds an element to the end of the list.
    
* `add(int index, E element)`: Inserts an element at the specified index.
    
* `get(int index)`: Retrieves the element at the specified index.
    
* `set(int index, E element)`: Replaces the element at the specified index with a new one.
    
* `remove(int index)`: Removes the element at the specified index.
    
* `indexOf(Object obj)`: Returns the index of the first occurrence of the specified element.
    
* `lastIndexOf(Object obj)`: Returns the index of the last occurrence of the specified element.
    
* `size()`: Returns the number of elements in the list.
    
* `isEmpty()`: Checks if the list is empty.
    
* `clear()`: Removes all elements from the list.
    
* `subList(int fromIndex, int toIndex)`: Returns a view of the list as a sublist from `fromIndex` (inclusive) to `toIndex` (exclusive).
    

**Common List Implementations:**

Java provides several implementations of the `List` interface to suit different use cases. Some common ones include:

**1\. ArrayList (java.util.ArrayList):**

* Backed by an array, which allows for fast random access.
    
* Efficient for most use cases, especially when the list size is known in advance.
    
* Dynamic resizing when the list grows.
    

**2\. LinkedList (java.util.LinkedList):**

* Implemented as a doubly-linked list, which allows for efficient insertions and removals at both ends.
    
* Less efficient than `ArrayList` for random access.
    
* Suitable when frequent insertions and deletions are required.
    

**3\. Vector (java.util.Vector):**

* Similar to `ArrayList` but is thread-safe (synchronized).
    
* Generally less efficient than `ArrayList` due to synchronization overhead.
    
* Used in multi-threaded environments when synchronization is required.
    

**4\. Stack (java.util.Stack):**

* A specialized implementation of a stack data structure.
    
* Extends `Vector` and is used for Last-In-First-Out (LIFO) operations.
    
* Consider using `Deque` for more flexibility and modern stack operations.
    

**Example of Using ArrayList:**

Here's an example of using `ArrayList`:

```java
import java.util.ArrayList;
import java.util.List;

public class ArrayListExample {
    public static void main(String[] args) {
        // Create an ArrayList of strings
        List<String> fruits = new ArrayList<>();

        // Add elements
        fruits.add("Apple");
        fruits.add("Banana");
        fruits.add("Cherry");

        // Access elements
        String firstFruit = fruits.get(0); // "Apple"

        // Modify elements
        fruits.set(1, "Grapes"); // Replaces "Banana" with "Grapes"

        // Remove an element
        fruits.remove(2); // Removes "Cherry"

        // Iterate through the list
        for (String fruit : fruits) {
            System.out.println(fruit);
        }
    }
}
```

The `List` interface and its implementations provide flexible and versatile options for managing ordered collections of data in Java. You can choose the appropriate implementation based on your specific requirements and performance considerations.