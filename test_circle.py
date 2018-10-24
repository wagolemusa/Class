import unittest
from circle import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
	def test_area(self):

		# test areas when radius >= 0
		self.assertEqual(circle_area(1), pi)
		self.assertEqual(circle_area(0), 0)
		self.assertEqual(circle_area(2.1), pi * 2.1**2)

	def test_values(self):
		# Make sure values errors are raised when necessary
		self.assertRaises(ValueError, circle_area, 2)


if __name__ == '__main__':
	unittest.main()