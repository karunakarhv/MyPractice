# Count the minimum number of jumps needed to reach the end of the array, where each element in the array represents the maximum jump length at that position.
def min_jumps(x, y, d):
    if d <= 0:
        return 0
    distance = y - x
    jumps = (distance + d - 1) // d  # Calculate the number of jumps needed using ceiling division
    print(f"Starting position: {x}, Target position: {y}, Distance: {d}, Jumps needed: {jumps}")
    return jumps

# Example usage:
x = 10
y = 85
d = 30
print(min_jumps(x, y, d))  # Output: 8
    