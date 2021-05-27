import unittest
from string_print import my_full_name


class TestCircleArea(unittest.TestCase):
  def test_string_my_full_name(self):
    # Testa retorno de uma string na função full_name
    self.assertAlmostEqual(type(my_full_name()), str)
