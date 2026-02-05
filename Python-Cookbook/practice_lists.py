# Learn about lists in Python by completing the functions below. You can run this file to test your code.
# 1. Create a function that takes in a list of numbers and returns the sum of all the numbers in the list.
def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# 2. Create a function that takes in a list of strings and returns a new list with all the strings in uppercase.
def uppercase_strings(strings):
    uppercase_list = []
    for string in strings:
        uppercase_list.append(string.upper())
    return uppercase_list

# 3. Create a function that takes in a list of numbers and returns a new list with only the even numbers.
def even_numbers(numbers):
    even_list = []
    for number in numbers:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

# 4. Create a function that takes in a list of strings and returns a new list with only the strings that start with the letter 'A'.
def strings_starting_with_a(strings):
    a_strings = []
    for string in strings:
        if string.startswith('A'):
            a_strings.append(string)
    return a_strings

# 5. Create a function that takes in a list of numbers and returns the largest number in the list.
def largest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Test your functions
if __name__ == "__main__":
    # Assert statements to test the functions
    assert sum_of_numbers([1, 2, 3, 4, 5]) == 15, "Test failed: sum_of_numbers([1, 2, 3, 4, 5]) should return 15"
    assert uppercase_strings(["hello", "world"]) == ['HELLO', 'WORLD'], "Test failed: uppercase_strings(['hello', 'world']) should return ['HELLO', 'WORLD']"
    assert even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6], "Test failed: even_numbers([1, 2, 3, 4, 5, 6]) should return [2, 4, 6]"
    assert strings_starting_with_a(["Apple", "Banana", "Avocado", "Cherry"]) == ['Apple', 'Avocado'], "Test failed: strings_starting_with_a(['Apple', 'Banana', 'Avocado', 'Cherry']) should return ['Apple', 'Avocado']"
    assert largest_number([1, 2, 3, 4, 5]) == 5, "Test failed: largest_number([1, 2, 3, 4, 5]) should return 5"
    print("All tests passed!")