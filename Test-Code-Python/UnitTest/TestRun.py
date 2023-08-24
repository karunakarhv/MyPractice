import unittest
import xmlrunner
from TestSuite import TestSuite

def main():
    testRunner = xmlrunner.XMLTestRunner(output='test-reports', verbosity=2)
    suite = unittest.TestSuite()
    MasterDataSourcesSuite = TestSuite.suite(suite)
    testRunner.run(MasterDataSourcesSuite)

if __name__ == '__main__':
    main()