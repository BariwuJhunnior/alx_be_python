import unittest
from simple_calculator import SimpleCalculator

class test_simple_calculator(unittest.TestCase):

  def setUp(self):
    self.calc = SimpleCalculator()

  def test_addition(self):
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)
    self.assertEqual(self.calc.add(-10, 2), -8)

  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(10, 2), 8)
    self.assertEqual(self.calc.subtract(-1, 1), -2)
    self.assertEqual(self.calc.subtract(0, 4), -4)

  def test_multiplication(self):
    self.assertEqual(self.calc.multiply(2, 4), 8)
    self.assertEqual(self.calc.multiply(2, 0), 0)
    self.assertEqual(self.calc.multiply(-2, 4), -2)

  def test_division(self):
    self.assertEqual(self.calc.divide(4, 2), 2)
    self.assertEqual(self.calc.divide(10, 0), ZeroDivisionError)
    self.assertEqual(self.calc.divide(13, 8), 1.625)



