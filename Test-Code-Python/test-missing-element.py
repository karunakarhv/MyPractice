# 
def missing_element(lst):
    n = len(lst) + 1  # Total number of elements including the missing one
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(lst)  # Sum of the given list
    missing_number = total_sum - actual_sum  # The missing number is the difference
    print(f"Total sum (1 to {n}): {total_sum}, Actual sum: {actual_sum}, Missing number: {missing_number}")
    return missing_number

# Example usage:
lst = [1, 2, 4, 5]
print(missing_element(lst))  # Output: 3