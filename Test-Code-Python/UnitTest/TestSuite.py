import unittest
import TestCase
import TestData

class TestSuite(unittest.TestSuite):

    def suite(self):
        suite = unittest.TestSuite()
        sequence = 0
        for api_test in TestData.COMPLETE_TESTS:
            suite.addTest(TestCase.ExampleTestCase(api_test))
            sequence += 1
        return suite