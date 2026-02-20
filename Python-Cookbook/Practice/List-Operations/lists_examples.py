# Basic list creation
fruits = ["apple", "banana", "orange"]
print("Fruits:", fruits)

# Appending an item
fruits.append("grape")
print("After append:", fruits)

# Removing an item
fruits.remove("banana")
print("After remove:", fruits)

# Slicing a list
print("First two fruits:", fruits[:2])

# List comprehension - creating a list of squares
squares = [x**2 for x in range(5)]
print("Squares:", squares)

# Checking membership
if "apple" in fruits:
    print("Apple is in the list.")

# Iterating through a list
for fruit in fruits:
    print("Fruit:", fruit)

# List length
print("Number of fruits:", len(fruits))

# Sorting a list
fruits.sort()
print("Sorted fruits:", fruits)