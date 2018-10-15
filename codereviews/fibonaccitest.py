import unittest
from fibonacci import *
class testFibonacciNumbers(unittest.TestCase):
    
    def test_fibonaccil(self):
        self.assertEqual(fibNumbers().fibonaccil(10),
        [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])

    def test_sum_of_even_fibonacci(self):
        self.assertEqual(fibNumbers().sum_even_fibonaccil(10),44)
        self.assertEqual(fibNumbers().sum_even_fibonaccil(),4613732)
if __name__ == '__main__':
    unittest.main()