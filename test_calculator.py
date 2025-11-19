#https://github.com/alberto-sclocchi/lab11-AS-MM.git
# Partner 1: Alberto Sclocchi
# Partner 2: Matias Mena Gorostiaga

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(2, -3), -6)
        self.assertEqual(multiply(2, 0), 0)
        self.assertEqual(multiply(2, 1), 2)
        self.assertEqual(multiply(-2, -2), 4)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 6), 3)
        self.assertEqual(div(-3, 6), -2)
        self.assertEqual(div(2,0), 0)
        self.assertEqual(div(1, 2), 2)
        self.assertEqual(div(-2, -2), 1)

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -5)
        with self.assertRaises(ValueError):
            logarithm(2, 0)

    def test_hypotenuse(self):
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(4, -3), 5)
        self.assertEqual(hypotenuse(4, 0), 4)
        self.assertAlmostEqual(hypotenuse(4, 1), 4.123105625617661)


    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-5)

# Do not touch this
if __name__ == "__main__":
    unittest.main()