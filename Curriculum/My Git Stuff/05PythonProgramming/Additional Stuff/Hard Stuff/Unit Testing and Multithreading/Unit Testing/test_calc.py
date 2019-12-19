'''
Any file we want to user for testing needs to have test_ in front of the file name. 
The unittest library needs it
'''
import unittest
import calc


# Inherit from the unittest.Testcase()
class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(8,9), 17)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,9), 1)
        self.assertEqual(calc.subtract(1,-1), 2)
        self.assertEqual(calc.subtract(-1,-1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(2,9), 18)
        self.assertEqual(calc.multiply(0,1), 0)
        self.assertEqual(calc.multiply(1,10), 10)

    def test_divide(self):
        self.assertEqual(calc.divide(20,2), 10)
        self.assertEqual(calc.divide(1,1), 1)
        self.assertEqual(calc.divide(100,10), 10)

if __name__ == "__main__":
    unittest.main()
