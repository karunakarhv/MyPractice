def unpaired(array):
    result = 0
    for number in array:
        print(f"Current number: {number}, current result: {result}")
        result ^= number  # XOR operation to find the unpaired element
        print(f"Updated result after XOR: {result}")
    return result

# Example usage:
array = [9, 3, 9, 3, 9, 7, 9]
print(unpaired(array))  # Output: 7