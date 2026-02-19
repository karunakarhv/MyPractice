---
title: "SortedMap Interface in Java"
datePublished: Thu Sep 21 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clmts058o000508ma8acjbsxt
slug: sortedmap-interface-in-java
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1695296775085/6ea7917a-b070-4ee0-9f64-b79861a641ef.png
tags: java, java-beginner

---

In Java, the `SortedMap` interface is part of the Java Collections Framework and extends the `Map` interface. It represents a map that maintains its entries in a sorted order based on the keys. Unlike the standard `Map` interface, which does not guarantee any specific order of keys, a `SortedMap` ensures that the keys are sorted according to their natural order or a custom comparator provided during map creation. This makes `SortedMap` useful when you need to work with key-value pairs in a specific order. Here's an overview of the `SortedMap` interface and some common implementations:

**1\. SortedMap Interface (java.util.SortedMap):**

The `SortedMap` interface defines methods for managing key-value pairs while maintaining a sorted order of keys:

* `comparator()`: Returns the comparator used to order the keys, or `null` if the natural ordering of keys is used.
    
* `subMap(K fromKey, K toKey)`: Returns a view of the portion of the map whose keys range from `fromKey` (inclusive) to `toKey` (exclusive).
    
* `headMap(K toKey)`: Returns a view of the portion of the map whose keys are less than `toKey`.
    
* `tailMap(K fromKey)`: Returns a view of the portion of the map whose keys are greater than or equal to `fromKey`.
    
* `firstKey()`: Returns the first (lowest) key in the map.
    
* `lastKey()`: Returns the last (highest) key in the map.
    

**Common SortedMap Implementations:**

Java provides several implementations of the `SortedMap` interface to suit different use cases. Some common ones include:

**1\. TreeMap (java.util.TreeMap):**

* Implemented as a Red-Black tree, which ensures that key-value pairs are sorted according to their keys.
    
* Allows the use of a custom comparator for sorting.
    
* Supports efficient retrieval of key-value pairs in sorted order.
    
* Suitable when you need a map with keys in sorted order.
    

**Example of Using TreeMap as a SortedMap:**

Here's an example of using `TreeMap` as a `SortedMap`:

```java
import java.util.SortedMap;
import java.util.TreeMap;

public class TreeMapExample {
    public static void main(String[] args) {
        // Create a TreeMap of names and ages
        SortedMap<String, Integer> ages = new TreeMap<>();

        // Add key-value pairs
        ages.put("Alice", 25);
        ages.put("Bob", 30);
        ages.put("Charlie", 22);

        // Retrieve values by key
        int aliceAge = ages.get("Alice"); // 25

        // Check if a key exists
        boolean hasKey = ages.containsKey("David"); // false

        // Iterate through the key-value pairs in sorted order
        for (String name : ages.keySet()) {
            int age = ages.get(name);
            System.out.println("Name: " + name + ", Age: " + age);
        }
    }
}
```

In the example above, the `TreeMap` maintains the key-value pairs in sorted order based on the keys. This allows you to retrieve entries in sorted order, which can be useful for various applications, such as maintaining a sorted dictionary or addressing cases where keys need to be processed in a specific order.