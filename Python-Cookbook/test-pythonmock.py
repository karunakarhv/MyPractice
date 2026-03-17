# Write Python Mock Tests
import unittest
from unittest.mock import MagicMock

class MyClass:
    def method_to_mock(self):
        return "Original Method"
    
class TestMyClass(unittest.TestCase):
    def test_method_to_mock(self):
        # Create an instance of MyClass
        my_instance = MyClass()
        
        # Mock the method_to_mock
        my_instance.method_to_mock = MagicMock(return_value="Mocked Method")
        
        # Call the mocked method
        result = my_instance.method_to_mock()
        
        # Assert that the mocked method returns the expected value
        self.assertEqual(result, "Mocked Method")
        
        # Assert that the mocked method was called once
        my_instance.method_to_mock.assert_called_once()
if __name__ == '__main__':    
    unittest.main()
    
    # Use patch and Mock class to mock a function in a module
from unittest.mock import patch, Mock
def function_to_mock():
    return "Original Function"
class TestFunctionToMock(unittest.TestCase):
    @patch('__main__.function_to_mock')
    def test_function_to_mock(self, mock_function):
        # Set the return value of the mocked function
        mock_function.return_value = "Mocked Function"
        
        # Call the mocked function
        result = function_to_mock()
        
        # Assert that the mocked function returns the expected value
        self.assertEqual(result, "Mocked Function")
        
        # Assert that the mocked function was called once
        mock_function.assert_called_once()