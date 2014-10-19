import unittest
from sudoku_solved import check_row, check_square, sudoku_solved


class SudokuSolvedTest(unittest.TestCase):

    def test_check_row(self):
        self.assertTrue(check_row([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]))
        self.assertFalse(check_row([
            [1, 2, 3, 4, 5, 5, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]))

    def test_check_square(self):
        self.assertTrue(check_square([
            [4, 5, 2, 3, 8, 9, 7, 1, 6],
            [3, 8, 7, 4, 6, 1, 2, 9, 5],
            [6, 1, 9, 2, 5, 7, 3, 4, 8],
            [9, 3, 5, 1, 2, 6, 8, 7, 4],
            [7, 6, 4, 9, 3, 8, 5, 2, 1],
            [1, 2, 8, 5, 7, 4, 6, 3, 9],
            [5, 7, 1, 8, 9, 2, 4, 6, 3],
            [8, 9, 6, 7, 4, 3, 1, 5, 2],
            [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]))
        self.assertFalse(check_square([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]))

    def test_sudoku_solved(self):
        self.assertTrue(sudoku_solved([
            [4, 5, 2, 3, 8, 9, 7, 1, 6],
            [3, 8, 7, 4, 6, 1, 2, 9, 5],
            [6, 1, 9, 2, 5, 7, 3, 4, 8],
            [9, 3, 5, 1, 2, 6, 8, 7, 4],
            [7, 6, 4, 9, 3, 8, 5, 2, 1],
            [1, 2, 8, 5, 7, 4, 6, 3, 9],
            [5, 7, 1, 8, 9, 2, 4, 6, 3],
            [8, 9, 6, 7, 4, 3, 1, 5, 2],
            [2, 4, 3, 6, 1, 5, 9, 8, 7]
        ]))
        self.assertFalse(sudoku_solved([
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ]))


if __name__ == '__main__':
    unittest.main()
