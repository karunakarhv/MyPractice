---
title: "Parameterization in Pytest: Running Tests with Multiple Inputs"
datePublished: Sat Sep 16 2023 23:00:12 GMT+0000 (Coordinated Universal Time)
cuid: clmmmsvrq000409jx1vqbei11
slug: parameterization-in-pytest-running-tests-with-multiple-inputs
cover: https://cdn.hashnode.com/res/hashnode/image/upload/v1694862956735/d2bbca9d-afb5-404e-b7da-25b5837667fe.jpeg
tags: python, python-beginner

---

Parameterization in Pytest allows you to run the same test function with multiple sets of inputs or arguments. This is a powerful feature that helps you efficiently test a wide range of scenarios without writing redundant test functions. Parameterization is often used in unit testing to cover different cases.

Here's how you can use parameterization in Pytest:

**Using the** `@pytest.mark.parametrize` Decorator:

You can use the `@pytest.mark.parametrize` decorator to define the parameters and the corresponding test cases for your test function.

Here's an example:

```python
import pytest

@pytest.mark.parametrize("input, expected", [
    (1, 2),   # Test Case 1
    (2, 4),   # Test Case 2
    (0, 0),   # Test Case 3
    (-1, 1),  # Test Case 4
])
def test_multiply_by_two(input, expected):
    result = input * 2
    assert result == expected
```

In this example, the `test_multiply_by_two` function is parameterized with two arguments, `input` and `expected`. Each tuple within the list represents a test case. Pytest will run the test function four times with the provided inputs and expected outputs.

**Running the Parameterized Tests:**

To run parameterized tests with Pytest, you can use the `pytest` command as usual:

```bash
pytest my_tests.py
```

Pytest will automatically discover and execute parameterized tests.

**Dynamic Parameterization:**

You can also dynamically generate parameterized test cases based on some logic. For example, you can use a loop to generate test cases from a list of inputs and expected outputs:

```python
import pytest

test_cases = [
    (1, 2),
    (2, 4),
    (0, 0),
    (-1, 1),
]

@pytest.mark.parametrize("input, expected", test_cases)
def test_multiply_by_two(input, expected):
    result = input * 2
    assert result == expected
```

**Combining with Fixtures:**

Parameterization can be combined with fixtures to create more complex test scenarios. You can use fixtures to set up preconditions for each test case while still reusing the same test function.

Here's an example combining parameterization with a fixture:

```python
import pytest

@pytest.fixture(params=[1, 2, 3])
def input_data(request):
    return request.param

@pytest.mark.parametrize("input, expected", [
    (1, 2),   # Test Case 1
    (2, 4),   # Test Case 2
    (3, 6),   # Test Case 3
])
def test_multiply_by_two(input, expected, input_data):
    result = input * 2
    assert result == expected + input_data
```

In this example, the `input_data` fixture provides different values (1, 2, 3) as the `input` parameter for each test case.

Parameterization in Pytest is a valuable tool for efficiently testing various scenarios with minimal code duplication. It helps you cover multiple cases in a clean and organized way, improving test coverage and effectiveness.