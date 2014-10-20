import unittest
from simplify_fraction import is_prime, prime_possible_delimeters, \
    simplify_fraction


class SimplifyFractionTest(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(23))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(15))

    def test_prime_possible_delimeters(self):
        self.assertEqual([11], prime_possible_delimeters(11))
        self.assertEqual([13], prime_possible_delimeters(13))
        self.assertEqual([3,7], prime_possible_delimeters(21))


    def test_simplify_fraction(self):
        self.assertEqual((1, 3), simplify_fraction((3, 9)))
        self.assertEqual((1, 7), simplify_fraction((1, 7)))
        self.assertEqual((2, 5), simplify_fraction((4, 10)))
        self.assertEqual((3, 22), simplify_fraction((63, 462)))


if __name__ == '__main__':
    unittest.main()
