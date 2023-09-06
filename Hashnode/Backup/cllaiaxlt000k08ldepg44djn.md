---
title: "Lambda Function in Python"
datePublished: Mon Aug 14 2023 06:41:20 GMT+0000 (Coordinated Universal Time)
cuid: cllaiaxlt000k08ldepg44djn
slug: lambda-function-in-python
cover: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/ZIPFteu-R8k/upload/3727ea9625f00b9681dad27709cb5147.jpeg
tags: python, developer

---

A lambda function in Python is a small, anonymous function defined using the `lambda` keyword. Lambda functions are often used when you need a simple function for a short period and don't want to define a full function using the `def` keyword. Lambda functions are also known as anonymous functions because they don't require a name.

The syntax of a lambda function is as follows:

```python
lambda arguments: expression
```

Here are some examples of using lambda functions in various scenarios:

**Example 1: Basic Lambda Function**

```python
# A lambda function that adds two numbers
add = lambda x, y: x + y

result = add(5, 3)
print(result)  # Output: 8
```

**Example 2: Sorting with Lambda Function**

```python
# A list of tuples containing names and ages
people = [('Alice', 25), ('Bob', 30), ('Charlie', 22)]

# Sort the list based on the second element of each tuple (age)
people_sorted = sorted(people, key=lambda x: x[1])

print(people_sorted)
# Output: [('Charlie', 22), ('Alice', 25), ('Bob', 30)]
```

**Example 3: Using Lambda with** `map()`

```python
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Use lambda with map to square each number
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)
# Output: [1, 4, 9, 16, 25]
```

**Example 4: Using Lambda with** `filter()`

```python
# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use lambda with filter to get even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
# Output: [2, 4, 6, 8, 10]
```

**Example 5: Using Lambda in a Custom Function**

```python
# A function that generates another function using a lambda function
def power_function(power):
    return lambda x: x ** power

square = power_function(2)
cube = power_function(3)

print(square(4))  # Output: 16
print(cube(3))    # Output: 27
```

Keep in mind that while lambda functions can be convenient for simple operations, using `def` to define named functions is recommended for more complex operations and for functions that you might need to reuse multiple times.