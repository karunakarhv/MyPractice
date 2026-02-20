# List: ordered, mutable, allows duplicates
my_list = [1, 2, 2, 3]
print("List:", my_list)
my_list[0] = 10             # Change value at index 0
my_list.append(4)           # Add a new element
print("Modified List:", my_list)
print("Second slice:", my_list[1:3])  # Slicing works

# Tuple: ordered, immutable, allows duplicates
my_tuple = (1, 2, 2, 3)
print("\nTuple:", my_tuple)
# my_tuple[0] = 10          # Uncommenting this line would raise a TypeError!
print("Tuple count of 2:", my_tuple.count(2))  # Tuples support count and index

# Set: unordered, mutable, **no duplicates**
my_set = {1, 2, 2, 3}
print("\nSet:", my_set)     # Output: {1, 2, 3}; duplicate '2' removed
my_set.add(4)               # Add a new element to the set
print("Set after adding 4:", my_set)
# print(my_set[0])          # Uncommenting this line would raise a TypeError (sets are not indexable)
my_set.remove(2)            # Remove element

# Set operations
another_set = {3, 4, 5}
print("Union:", my_set | another_set)         # {1, 3, 4, 5}
print("Intersection:", my_set & another_set)  # {3, 4}
print("Difference:", my_set - another_set)    # {1}

# Membership testing (fast with sets)
print("\nIs 3 in set?", 3 in my_set)          # True
print("Is 2 in set?", 2 in my_set)            # False (since we've removed 2)