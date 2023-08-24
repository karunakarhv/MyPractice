import unittest

class ExampleTestCase(unittest.TestCase):

    def __init__(self, test_data):
        super(ExampleTestCase, self).__init__()
        self.test_data = test_data

    def id(self):
        return "APITests." + str(self.__class__.__name__) + "." + str(self.test_data["name"] + "_(" +str(self.test_data["desc"]) + ")")

    def runTest(self):
        print('HelloWorld')
        self.assertNotEquals('TC_GET_VALID_SINGLE_CONNECTOR', self.test_data['name'])
