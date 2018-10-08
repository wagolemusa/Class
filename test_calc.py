import unittest

import functiontest

class TestCalc(unittest.TestCase):


	# def test_add(self):
	# 	result = functiontest.add(40, 20)
	# 	self.assertEqual(result, 60)

	def test_add(self):
		self.assertEqual(functiontest.add(40, 20), 60)
		self.assertEqual(functiontest.add(-1, 1), 0)
		self.assertEqual(functiontest.add(-1, -1), -2)

	def test_subtract(self):
		self.assertEqual(functiontest.subtract(10, 5), 5)
		self.assertEqual(functiontest.subtract(-1, 1), -2)
		self.assertEqual(functiontest.subtract(-1, -1), 0)


	def test_multipy(self):
		self.assertEqual(functiontest.multiply(10, 5), 50)
		self.assertEqual(functiontest.multiply(-1, 1), -1)
		self.assertEqual(functiontest.multiply(-1, -1), 1)

	def test_divide(self):
			self.assertEqual(functiontest.divide(10, 5), 2)
			self.assertEqual(functiontest.divide(-1, 1), -1)
			self.assertEqual(functiontest.divide(-1, -1), 1)

if __name__ == '__main__':
	unittest.main()