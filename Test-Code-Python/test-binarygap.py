import pytest
# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded 
# by ones at both ends in the binary representation of N.

def binary_gap(N):
    binary_representation = bin(N)[2:]  # Get binary representation as a string, excluding the '0b' prefix
    max_gap = 0
    current_gap = 0
    found_one = False

    for digit in binary_representation:
        if digit == '1':
            if found_one:
                print(f"Found a '1', current gap: {current_gap}, max gap: {max_gap}")
                max_gap = max(max_gap, current_gap)
            found_one = True
            current_gap = 0  # Reset gap count after finding a '1'
        elif found_one:  # Only count zeros if we've found at least one '1'
            current_gap += 1

    return max_gap
# Write pytest test cases to validate the binary_gap function
test_values = [
    (9, 2),    # Binary: 1001
    (529, 4),  # Binary: 1000010001
    (20, 1),   # Binary: 10100
    (15, 0),   # Binary: 1111
    (32, 0)    # Binary: 100000
]
@pytest.mark.parametrize("input_value, expected_output", test_values)
def test_binary_gap(input_value, expected_output):
    assert binary_gap(input_value) == expected_output