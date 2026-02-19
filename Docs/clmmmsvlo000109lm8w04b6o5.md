---
title: "Deque Interface in Java"
datePublished: Sat Sep 16 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clmmmsvlo000109lm8w04b6o5
slug: deque-interface-in-java
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1694863298799/95354e06-1593-4aca-a946-2eccebe04fd2.png
tags: java, java-beginner

---

In Java, the `Deque` (pronounced "deck") interface is part of the Java Collections Framework and represents a double-ended queue. A deque is a linear collection that allows elements to be inserted and removed from both ends, making it suitable for a wide range of applications, including queues and stacks. The `Deque` interface extends the `Queue` interface and defines methods for adding, removing, and inspecting elements at both ends of the collection. Here's an overview of the `Deque` interface and some common implementations:

**1\. Deque Interface (java.util.Deque):**

The `Deque` interface defines the following key methods:

* **Adding Elements:**
    
    * `addFirst(E element)`: Inserts an element at the beginning of the deque. Throws an exception if the operation fails.
        
    * `addLast(E element)`: Inserts an element at the end of the deque. Throws an exception if the operation fails.
        
    * `offerFirst(E element)`: Inserts an element at the beginning of the deque. Returns `true` if the operation was successful, `false` otherwise.
        
    * `offerLast(E element)`: Inserts an element at the end of the deque. Returns `true` if the operation was successful, `false` otherwise.
        
* **Removing Elements:**
    
    * `removeFirst()`: Removes and returns the element at the beginning of the deque. Throws an exception if the deque is empty.
        
    * `removeLast()`: Removes and returns the element at the end of the deque. Throws an exception if the deque is empty.
        
    * `pollFirst()`: Removes and returns the element at the beginning of the deque. Returns `null` if the deque is empty.
        
    * `pollLast()`: Removes and returns the element at the end of the deque. Returns `null` if the deque is empty.
        
* **Inspecting Elements:**
    
    * `getFirst()`: Retrieves, but does not remove, the element at the beginning of the deque. Throws an exception if the deque is empty.
        
    * `getLast()`: Retrieves, but does not remove, the element at the end of the deque. Throws an exception if the deque is empty.
        
    * `peekFirst()`: Retrieves, but does not remove, the element at the beginning of the deque. Returns `null` if the deque is empty.
        
    * `peekLast()`: Retrieves, but does not remove, the element at the end of the deque. Returns `null` if the deque is empty.
        
* **Size and Empty Check:**
    
    * `size()`: Returns the number of elements in the deque.
        
    * `isEmpty()`: Checks if the deque is empty.
        
* **Iterating and Traversing:**
    
    * `iterator()`: Returns an iterator to traverse the elements in the deque.
        

**Common Deque Implementations:**

Java provides several implementations of the `Deque` interface to suit different use cases. Some common ones include:

**1\. ArrayDeque (java.util.ArrayDeque):**

* Implemented as a resizable array and can be used as a general-purpose deque.
    
* Provides fast insertions and removals at both ends (front and back).
    
* Suitable for a wide range of applications.
    

**2\. LinkedList (java.util.LinkedList):**

* Implements a doubly-linked list and can be used as a deque or a general-purpose list.
    
* Supports efficient insertions and removals at both ends.
    
* Can also function as a `Queue` or `List` depending on how elements are added and removed.
    

**Example of Using ArrayDeque as a Deque:**

Here's an example of using `ArrayDeque` as a deque:

```java
import java.util.ArrayDeque;
import java.util.Deque;

public class DequeExample {
    public static void main(String[] args) {
        // Create a deque of integers
        Deque<Integer> deque = new ArrayDeque<>();

        // Add elements to the front and back
        deque.addFirst(1);
        deque.addLast(2);
        deque.offerFirst(0);

        // Remove elements from the front and back
        int first = deque.pollFirst(); // 0
        int last = deque.removeLast(); // 2

        // Peek at elements at the front and back
        int frontElement = deque.peekFirst(); // 1
        int backElement = deque.getLast(); // 1

        // Iterate through the deque
        for (int num : deque) {
            System.out.println(num);
        }
    }
}
```

The `Deque` interface and its implementations are versatile and can be used for various data structures, including queues, stacks, and double-ended queues. Depending on your specific requirements, you can choose the appropriate implementation for your application.