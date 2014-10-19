import unittest
from simplify_fraction import is_prime, prime_possible_delimeters, simplify_fraction

class SimplifyFractionTest(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(27))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(15))

    def test_prime_possible_delimeters(self):
        

if __name__ == '__main__':
    unittest.main()