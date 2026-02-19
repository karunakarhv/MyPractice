---
title: "Queue Interface in Java"
datePublished: Fri Sep 15 2023 23:00:09 GMT+0000 (Coordinated Universal Time)
cuid: clml7cyx8000709md4tqmhwhi
slug: queue-interface-in-java
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1694778457961/2d51a51b-e202-4f72-882a-7fa38b68d62d.png
tags: java, java-beginner

---

In Java, the `Queue` interface is part of the Java Collections Framework and represents a linear collection of elements where elements are inserted and removed in a specific order. Queues follow the First-In-First-Out (FIFO) principle, meaning that the element inserted first will be the first one to be removed. The `Queue` interface extends the `Collection` interface and defines several methods for adding, removing, and inspecting elements. Here's an overview of the `Queue` interface and some common implementations:

**1\. Queue Interface (java.util.Queue):**

The `Queue` interface defines the following key methods:

* `add(E element)`: Adds an element to the queue. Throws an exception if the operation fails.
    
* `offer(E element)`: Adds an element to the queue. Returns `true` if the operation was successful, `false` otherwise.
    
* `remove()`: Removes and returns the head (front) element of the queue. Throws an exception if the queue is empty.
    
* `poll()`: Removes and returns the head element of the queue. Returns `null` if the queue is empty.
    
* `element()`: Retrieves, but does not remove, the head element of the queue. Throws an exception if the queue is empty.
    
* `peek()`: Retrieves, but does not remove, the head element of the queue. Returns `null` if the queue is empty.
    
* `size()`: Returns the number of elements in the queue.
    
* `isEmpty()`: Checks if the queue is empty.
    
* `clear()`: Removes all elements from the queue.
    

**Common Queue Implementations:**

Java provides several implementations of the `Queue` interface to suit different use cases. Some common ones include:

**1\. LinkedList (java.util.LinkedList):**

* Implements a doubly-linked list and can be used as a general-purpose queue.
    
* Supports efficient insertions and removals at both ends.
    
* Can also function as a `Deque` (double-ended queue) by adding elements at both ends.
    

**2\. PriorityQueue (java.util.PriorityQueue):**

* Implemented as a priority heap (binary heap).
    
* Orders elements based on their natural order (or according to a custom comparator).
    
* Allows efficient retrieval of the highest-priority element.
    
* Suitable for applications where elements have associated priorities.
    

**3\. ArrayDeque (java.util.ArrayDeque):**

* Implemented as a resizable array and can be used as a general-purpose queue or stack.
    
* Provides fast insertions and removals at both ends (front and back).
    
* Can function as both a queue and a stack depending on how elements are added and removed.
    

**Example of Using LinkedList as a Queue:**

Here's an example of using `LinkedList` as a queue:

```java
import java.util.LinkedList;
import java.util.Queue;

public class QueueExample {
    public static void main(String[] args) {
        // Create a queue of strings
        Queue<String> queue = new LinkedList<>();

        // Enqueue (add) elements
        queue.offer("Alice");
        queue.offer("Bob");
        queue.offer("Charlie");

        // Dequeue (remove and retrieve) elements
        String firstInLine = queue.poll(); // "Alice"

        // Peek (retrieve without removing) the head element
        String nextInLine = queue.peek(); // "Bob"

        // Iterate through the queue
        for (String person : queue) {
            System.out.println(person);
        }
    }
}
```

The `Queue` interface and its implementations are useful for managing elements in a way that follows the FIFO principle. Depending on your specific requirements, you can choose the appropriate implementation for your application.