import unittest

class Authentication():
    def __init__(self) -> None:
        pass

class BasicAuth(Authentication):
    def __init__(self) -> None:
        super().__init__()
        self.key = None
        self.secret = None

class OAuth(Authentication):
    def __init__(self) -> None:
        super().__init__()
        self.key = None
        self.secret = None

class BaseTestCase(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

class ConfirmResults(BaseTestCase):
    def compareStatus(self, expected, actual):
        self.assertTrue(expected, actual)

class TestEmployee(ConfirmResults):
    def test_name(self):
        myvar = 'Karun'
        self.compareStatus('Karun', myvar)
    def run_unittest(*classes)

if __name__ == '__main__':
    unittest.main()