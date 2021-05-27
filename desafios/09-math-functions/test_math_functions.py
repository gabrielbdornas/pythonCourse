import unittest
from math_functions import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
  def test_area_positive_radios(self):
  # testa área para raios >=0
    self.assertAlmostEqual(circle_area(1), (pi * 1**2))
    self.assertAlmostEqual(circle_area(0), (pi * 0**2))
    self.assertAlmostEqual(circle_area(2.1), (pi * 2.1**2))

  def test_value_errors(self):
    self.assertRaises(ValueError, circle_area, -2)

  def test_type_errors(self):
    self.assertRaises(TypeError, circle_area, 3+5j)
    self.assertRaises(TypeError, circle_area, True)
    self.assertRaises(TypeError, circle_area, False)

