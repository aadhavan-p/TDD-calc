from calculator import Calculator
import unittest

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        res = Calculator().add(4, 6)
        self.assertEqual(10, res)

    def test_multiply(self):
        res = Calculator().multiply(5, 8)
        self.assertEqual(40, res)

    def test_divide(self):
        res = Calculator().divide(63, 9)
        self.assertEqual(7, res)

    def test_subtract(self):
        res = Calculator().subtract(17, 5)
        self.assertEqual(12, res)

if __name__ == '__main__':
    unittest.main()