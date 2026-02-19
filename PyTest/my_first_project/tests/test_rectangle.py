import pytest
from src.rectangle import Rectangle

@pytest.mark.parametrize("width, height, expected_area", [
    (2, 3, 6),
    (5, 5, 25),
    (10, -5, -50)
])
def test_rectangle_area(width, height, expected_area):
    rectangle = Rectangle(width, height)
    assert rectangle.area() == expected_area

@pytest.mark.parametrize("width, height, expected_perimeter", [
    (2, 3, 10),
    (5, 5, 20),
    (10, -5, 0)
])
def test_rectangle_perimeter(width, height, expected_perimeter):
    rectangle = Rectangle(width, height)
    assert rectangle.perimeter() == expected_perimeter