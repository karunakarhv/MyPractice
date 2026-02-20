# Sum of n natural numbers
def sum_natural_numbers(n):
    if n < 0:
        return "Input must be a non-negative integer."
    return n * (n + 1) // 2
# Example usage:
n = 10
print(sum_natural_numbers(n))  # Output: 55

# Sum of n squares of n natural numbers
def sum_squares(n):
    if n < 0:
        return "Input must be a non-negative integer."
    return n * (n + 1) * (2 * n + 1) // 6
# Example usage:
n = 10
print(sum_squares(n))  # Output: 385

# Sum of n cubes of n natural numbers
def sum_cubes(n):
    if n < 0:
        return "Input must be a non-negative integer."
    return (n * (n + 1) // 2) ** 2
# Example usage:
n = 10
print(sum_cubes(n))  # Output: 3025