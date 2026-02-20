# Rotate an Array

def rotate_array(nums, k):
    
    # Check if the input array is empty    
    if not nums:
        return
    # Handle cases where k is greater than the length of the array
    k = k % len(nums)
    print(f"Rotating array: {nums} by {k} positions")
    nums[:] = nums[-k:] + nums[:-k]  # Rotate the array in place
# Example usage:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]

# Write pytest test cases to validate the rotate_array function
import pytest

test_values = [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
    ([1, 2, 3], 1, [3, 1, 2]),
    ([1, 2, 3], 3, [1, 2, 3]),
    ([1, 2, 3], 4, [3, 1, 2]),
    ([], 1, [])
]
@pytest.mark.parametrize("input_array, k, expected_output", test_values)
def test_rotate_array(input_array, k, expected_output):
    rotate_array(input_array, k)
    assert input_array == expected_output