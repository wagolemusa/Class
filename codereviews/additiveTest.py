import unittest
from additiv import *

class testAdditiveSequence(unittest.TestCase):
	
	def test_additive(self):
		self.assertEqual(Sequence().additive_number("66121830"),True)

	def test_notValid(self):
		self.assertEqual(Sequence().isValid("51123", "65463", "67556"))

if __name__ == '__main__':
    unittest.main()