import sys
import os

sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite, TextTestRunner
from Test.Scripts.testMainPage import MainPage
from Test.Scripts.testPrices import testPrices
from Test.Scripts.testSearch import testSearch
from Test.Scripts.testComment import testComment
from Test.Scripts.testLike import testLike


import testtools as testtools
if __name__ == "__main__":
    test_loader = TestLoader()
    test_suite = TestSuite((
        #test_loader.loadTestsFromTestCase(MainPage),
        #test_loader.loadTestsFromTestCase(testPrices),
        test_loader.loadTestsFromTestCase(testSearch),
        #test_loader.loadTestsFromTestCase(testComment),
        #test_loader.loadTestsFromTestCase(testLike),
    ))

    test_runnner = TextTestRunner(verbosity=2)
    test_runnner.run(test_suite)

    parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    parallel_suite.run(testtools.StreamResult())
