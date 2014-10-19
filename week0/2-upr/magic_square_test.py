import unittest
from magic_square import sum_list, check_row_sum, check_first_diagonal, check_second_diagonal, magic_square


class MagicSquareTest(unittest.TestCase):

    def test_sum_list(self):
        self.assertEqual(6, sum_list([1, 2, 3]))
        self.assertEqual(72, sum_list([22, 24, 26]))

    def test_check_row_sum(self):
        self.assertTrue(check_row_sum(15, [[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
        self.assertFalse(check_row_sum(16, [[16, 23, 17], [78, 32, 21]]))

    def test_check_first_diagonal(self):
        self.assertTrue(
            check_first_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15))
        self.assertFalse(
            check_first_diagonal([[6, 2, 3], [4, 5, 20], [7, 8, 10]], 15))

    def test_check_first_diagonal(self):
        self.assertTrue(
            check_second_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 15))
        self.assertFalse(
            check_second_diagonal([[6, 2, 3], [4, 5, 20], [4, 8, 10]], 15))

    def test_magic_square(self):
        self.assertTrue(magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
        self.assertTrue(
            magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]]))
        self.assertTrue(
            magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
        self.assertFalse(magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
        self.assertFalse(
            magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))

if __name__ == '__main__':
    unittest.main()
