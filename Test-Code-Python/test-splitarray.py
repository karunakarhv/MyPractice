def solution(A):
    total_sum = sum(A)
    left_sum = 0
    min_diff = float('inf')
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        if diff < min_diff:
              min_diff = diff
    return min_diff

# Test Cases
def test_solution():
    # Small Inputs
    assert solution([1, 2]) == 1
    assert solution([1, 2, 3]) == 0
    assert solution([-1, -2, -3]) == 0

    # Large Inputs
    assert solution([1] * 100000) == 0
    assert solution([-1000, 1000] * 50000) == 0

    # Performance Tests
    assert solution(list(range(1, 100001))) == 66232
    assert solution([1] * 100000) == 0

    # Edge Cases
    assert solution([-1000, 1000]) == 2000
    assert solution([5, 5, 5, 5]) == 0

    print("All test cases passed.")

test_solution()