# Use Monkey Patch in Pytest
import pytest
class MyClass:
    def method_to_mock(self):
        return "Original Method"
@pytest.fixture
def my_instance():
    return MyClass()
def test_method_to_mock(my_instance, monkeypatch):
    # Mock the method_to_mock using monkeypatch
    monkeypatch.setattr(my_instance, 'method_to_mock', lambda: "Mocked Method")
    
    # Call the mocked method
    result = my_instance.method_to_mock()
    
    # Assert that the mocked method returns the expected value
    assert result == "Mocked Method"
def function_to_mock():
    return "Original Function"
def test_function_to_mock(monkeypatch):
    # Mock the function_to_mock using monkeypatch
    monkeypatch.setattr('__main__.function_to_mock', lambda: "Mocked Function")
    
    # Call the mocked function
    result = function_to_mock()
    
    # Assert that the mocked function returns the expected value
    assert result == "Mocked Function"