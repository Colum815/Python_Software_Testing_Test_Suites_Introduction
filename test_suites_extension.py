"""
This file is an extension of the test_suites.py file. In this file I have included a class called TestMoreThanOne
which contains a collection of tests. In order to run all these tests in the terminal,
I have used the makeSuite function to initialize the suite and added the other test cases using addTests.
Next I have stored the run function of the TextTestRunner in a variable called result.
I can now use this variable called result to display different information about the tests ran.
By setting the verbosity =2 in the TestTextRunner object more information about each test ran is displayed.
I have purposely demonstrated 1 failure, 1 error, 1 skipped in the output in the terminal.


"""
import unittest
class TestSubtraction(unittest.TestCase):
    def runTest(self):
        self.assertEqual((4-5),-1)

class TestMultiplication(unittest.TestCase):

    def runTest(self):
        self.assertEqual((4 * 6), 24)
# -------------------------------------------------------------------------
class TestMoreThanOne(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1,1)

    def test_2(self):
        self.assertEqual(2, 2)

    def test_3(self):
        self.assertEqual(3, 3)

    def test_4(self):
        self.assertEqual(4, 4)

# -------------------------------------------------------------------------

class TestAddition(unittest.TestCase):
    @unittest.skip("Skip the Addition Test Case")
    def runTest(self):
        self.assertEqual((5 + 10), 15)


class TestDivision(unittest.TestCase):

    def runTest(self):
        self.assertEqual((7 / 0), 10)

class TestSquare(unittest.TestCase):

    def runTest(self):
        self.assertEqual((4 ** 2), 16.1)


if __name__ == '__main__':
    suite = unittest.makeSuite(TestMoreThanOne,'test')

    suite.addTests([TestSubtraction(),TestMultiplication(),TestAddition(), TestDivision(),TestSquare()])
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    print('Errors: ', result.errors)
    print('\nFailures: ', result.failures)
    print('\nSkipped Tests: ', result.skipped)
    print('\nNo. of Tests: ', result.testsRun)
    print('\nWas it a successful test?  ', result.wasSuccessful())