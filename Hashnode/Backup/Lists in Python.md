---
title: "Lists in Python"
datePublished: Mon Aug 14 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: cllbh9rkb000109mffwjladay
slug: lists-in-python
cover: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/ZIPFteu-R8k/upload/d527d45d96030f7c9c26cf2aa69aa045.jpeg
tags: programming-blogs, python

---

A list is a fundamental data structure in Python used to store collections of items. Lists are ordered, mutable (meaning you can change their contents after they're created), and can hold a mix of different data types. Lists are defined using square brackets `[]`, and the items inside the list are separated by commas.

Here's a basic example of creating a list:

```python
my_list = [1, 2, 3, 4, 5]
```

You can access individual elements in a list using indexing. The index of the first element is 0, the second element is 1, and so on. Negative indices count from the end of the list. For example:

```python
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3
print(my_list[-1])  # Output: 5 (last element)
```

You can also use slicing to access a range of elements in a list:

```python
print(my_list[1:4])  # Output: [2, 3, 4]
print(my_list[:3])   # Output: [1, 2, 3]
print(my_list[2:])   # Output: [3, 4, 5]
```

Lists are mutable, so you can change their elements using indexing:

```python
my_list[1] = 7
print(my_list)  # Output: [1, 7, 3, 4, 5]
```

You can use various built-in functions and methods to manipulate lists:

* `len(my_list)` returns the length of the list.
    
* `my_list.append(item)` adds an item to the end of the list.
    
* `my_list.insert(index, item)` inserts an item at a specific index.
    
* `my_list.remove(item)` removes the first occurrence of the specified item.
    
* `my_list.pop(index)` removes and returns the item at the specified index.
    
* `my_list.index(item)` returns the index of the first occurrence of the specified item.
    
* `item in my_list` checks if an item is in the list.
    
* `my_list.sort()` sorts the list in ascending order.
    

Here's an example demonstrating some of these methods:

```python
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')
fruits.insert(1, 'grape')
fruits.remove('banana')
popped_fruit = fruits.pop(2)
print(fruits)  # Output: ['apple', 'grape', 'orange']
print(popped_fruit)  # Output: 'cherry'
print('apple' in fruits)  # Output: True
fruits.sort()
print(fruits)  # Output: ['apple', 'grape', 'orange']
```

Remember that lists can contain any data type, including other lists. This allows you to create nested structures and more complex data representations.