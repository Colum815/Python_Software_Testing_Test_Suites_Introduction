"""
For my introduction into test suites I have created multiple classes containing very basic tests. (one test per class)
To run some or all of these tests in the terminal I have included the code to do so at the end.
First I create a suite then I decided to add just one test tot the suite by using '.addTest()'.
Then I decided to add the rest using '.addTests()'.

I then run the tests in the terminal using unittest.TextTestRunner().run(suite)
"""
import unittest
class TestSubtraction(unittest.TestCase):
    def runTest(self):
        self.assertEqual((4-5),-1)

class TestMultiplication(unittest.TestCase):

    def runTest(self):
        self.assertEqual((4 * 6), 24)


class TestAddition(unittest.TestCase):

    def runTest(self):
        self.assertEqual((5 + 10), 15)


class TestDivision(unittest.TestCase):

    def runTest(self):
        self.assertEqual((20 / 2), 10)

class TestSquare(unittest.TestCase):

    def runTest(self):
        self.assertEqual((4 ** 2), 16)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestSubtraction())
    suite.addTests([TestMultiplication(),TestAddition(), TestDivision(),TestSquare()])
    unittest.TextTestRunner().run(suite)

# -----------------------------------------BASIC TEST SUITE INTRODUCTION------------------------------------------------
# import unittest
#
#
# class TestString(unittest.TestCase):
#
#     def runTest(self):
#         self.assertEqual("r" * 2, 'rr')
#
#
# class TestUCase(unittest.TestCase):
#
#     def runTest(self):
#         self.assertEqual('PYTHON'.lower(), 'python')
#
#
# if __name__ == '__main__':
#     suite = unittest.TestSuite([TestString(), TestUCase()])
#     unittest.TextTestRunner().run(suite)

# -------------------------------------END OF BASIC TEST SUITE INTRODUCTION---------------------------------------------
