---
title: "Python Cloning or Copying a list"
datePublished: Sun Sep 20 2020 21:34:39 GMT+0000 (Coordinated Universal Time)
cuid: ckfbmchu2059f2zs1gtnk2civ
slug: python-cloning-or-copying-a-list
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1600638418163/VZ51kyg6B.jpeg
tags: python

---

# Using the Slice Operator

```python
listOriginal = [1, 2, 3, 4]
listCopied = listOriginal[:]
print("Original List:", listOriginal)
print("Copied List using slice operator:", listCopied)
```

# Using the Extend Operator

```python
listOriginal = [1, 2, 3, 4, 5]
listCopied = []
listCopied.extend(listOriginal)
print("Original List:", listOriginal)
print("Copied List using extend operator:", listCopied)
```

# Using the list

```python
listOriginal = [1, 2, 3, 4, 5, 6]
listCopied = []
listCopied = list(listOriginal)
print("Original List:", listOriginal)
print("Copied List using list class:", listCopied)
```

# Using the list comprehension

```python
listOriginal = [1, 2, 3, 4, 5, 6, 7]
listCopied = []
listCopied = [item for item in listOriginal]
print("Original List:", listOriginal)
print("Copied List using list comprehension:", listCopied)
```

# Using the append method

```python
listOriginal = [1, 2, 3, 4, 5, 6, 7, 8]
listCopied = []
for item in listOriginal:
    listCopied.append(item)
print("Original List:", listOriginal)
print("Copied List using list append method:", listCopied)
```

# Using the shallow copy method

```python
import copy

listOriginal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listCopied = []
listCopied = copy.copy(listOriginal)
print("Original List:", listOriginal)
print("Copied List using list shallow copy:", listCopied)
```

# Using the deep copy method

```python
import copy

listOriginal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listCopied = []
listCopied = copy.deepcopy(listOriginal)
print("Original List:", listOriginal)
print("Copied List using list deep copy:", listCopied)
```