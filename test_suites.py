"""
For my introduction into test suites I have created multiple classes containing very basic tests. (one test per class)
To run some or all of these tests in the terminal I have included the code to do so at the end.
First I create a suite then I decided to add just one test tot the suite by using '.addTest()'.
Then I decided to add the rest using '.addTests()'.

I then run the tests in the terminal using unittest.TextTestRunner().run(suite)

To run the suite in the terminal I wrote down these steps:

1 Include if __name__ = '__main__':
              unittest.main()
  in the python file so code can be printed out in the terminal.
  Open folder where the file you want is. Go to properties and copy location
2 Open Terminal which will be in a default directory.
3 cd into the new location to create the new directory with the file in it.
4 You are in the folder now. To run a file invoke the python interpreter by writing
  python 'space' then the name of the file with the .py extension.
5 After .py extension you can add 'space' -v for verbose mode which shows you clearer info on tests run.
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


