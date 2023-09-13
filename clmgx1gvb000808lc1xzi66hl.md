---
title: "Collection - Interfaces in Java"
datePublished: Tue Sep 12 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clmgx1gvb000808lc1xzi66hl
slug: collection-interfaces-in-java
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1694517754127/13414e65-4924-4063-b7d7-19e13911e2df.png
tags: java, java-beginner

---

In Java, the Collections Framework defines several core interfaces that provide a standardized way to work with collections of objects. These interfaces serve as the foundation for various types of collections such as lists, sets, and maps. Understanding these interfaces is crucial when working with collections in Java. Here are the key collection interfaces in Java:

**1\. Collection Interface:**

* `java.util.Collection`
    
* Represents a group of objects.
    
* Root interface for all collection types.
    
* Common methods include `add()`, `remove()`, `size()`, `isEmpty()`, `contains()`, and `iterator()`.
    

**2\. List Interface:**

* `java.util.List`
    
* Represents an ordered collection that allows duplicate elements.
    
* Allows access to elements by their index.
    
* Common implementations include `ArrayList`, `LinkedList`, and `Vector`.
    

**3\. Set Interface:**

* `java.util.Set`
    
* Represents a collection that does not allow duplicate elements.
    
* Does not provide access to elements by their index.
    
* Common implementations include `HashSet`, `LinkedHashSet`, and `TreeSet`.
    

**4\. SortedSet Interface:**

* `java.util.SortedSet`
    
* Extends the `Set` interface and maintains elements in sorted order.
    
* Common implementation is `TreeSet`.
    

**5\. NavigableSet Interface:**

* `java.util.NavigableSet`
    
* Extends the `SortedSet` interface and adds navigation methods.
    
* Allows forward and backward element navigation.
    
* Common implementation is `TreeSet`.
    

**6\. Queue Interface:**

* `java.util.Queue`
    
* Represents a collection designed for holding elements before processing.
    
* Supports operations like `add()`, `remove()`, and `element()`.
    

**7\. Deque Interface:**

* `java.util.Deque`
    
* Extends the `Queue` interface to support both FIFO and LIFO operations.
    
* Allows elements to be added or removed from both ends.
    
* Common implementation is `ArrayDeque`.
    

**8\. Map Interface:**

* [`java.util.Map`](http://java.util.Map)
    
* Represents a collection of key-value pairs.
    
* Keys are unique, and each key maps to a single value.
    
* Common implementations include `HashMap`, `LinkedHashMap`, and `TreeMap`.
    

**9\. SortedMap Interface:**

* `java.util.SortedMap`
    
* Extends the `Map` interface and maintains keys in sorted order.
    
* Common implementation is `TreeMap`.
    

**10\. NavigableMap Interface:**

* `java.util.NavigableMap`
    
* Extends the `SortedMap` interface and adds navigation methods.
    
* Allows forward and backward key navigation.
    
* Common implementation is `TreeMap`.
    

These collection interfaces provide a consistent and unified way to work with different types of collections in Java. Implementing classes for these interfaces offer specific behaviors and characteristics, making it easier to choose the appropriate collection type for your application's needs.

For example, if you need a list that allows duplicate elements and maintains the order of insertion, you can use the `List` interface with an `ArrayList` implementation. If you require a set that does not allow duplicates and does not maintain any specific order, you can use the `Set` interface with a `HashSet` implementation. The choice of interface and implementation depends on your specific use case and requirements.