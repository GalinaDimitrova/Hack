def check_row(matrix):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    checked_row = []
    for row in matrix:
        # make a copy of the row
        checked_row = list(row)
        checked_row.sort()
        if check != checked_row:
            return False
    return True


def check_square(matrix):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    square = [[]]
    # we make all squares as a new matrix, \
    # where every row == square 3x3 from the base matrix
    square = [matrix[0][:3] + matrix[1][:3] + matrix[2][:3]]
    square.append(matrix[0][3:6] + matrix[1][3:6] + matrix[2][3:6])
    square.append(matrix[0][6:] + matrix[1][6:] + matrix[2][6:])

    square.append(matrix[3][:3] + matrix[4][:3] + matrix[5][:3])
    square.append(matrix[3][3:6] + matrix[4][3:6] + matrix[5][3:6])
    square.append(matrix[3][6:] + matrix[4][6:] + matrix[5][6:])

    square.append(matrix[6][:3] + matrix[7][:3] + matrix[8][:3])
    square.append(matrix[6][3:6] + matrix[7][3:6] + matrix[8][3:6])
    square.append(matrix[6][6:] + matrix[7][6:] + matrix[8][6:])

    if check_row(square) == False:
        return False
    else:
        return True


def sudoku_solved(sudoku):
    transposed = []
    for i in range(len(sudoku[0])):
        transposed.append([row[i] for row in sudoku])
    if check_row(sudoku) == False:
        print(False)
        return False
    elif check_row(transposed) == False:
        print(False)
        return False
    elif check_square(sudoku) == False:
        print(False)
        return False
    else:
        print(True)
        return True


sudoku_solved([
    [4, 5, 2, 3, 8, 9, 7, 1, 6],
    [3, 8, 7, 4, 6, 1, 2, 9, 5],
    [6, 1, 9, 2, 5, 7, 3, 4, 8],
    [9, 3, 5, 1, 2, 6, 8, 7, 4],
    [7, 6, 4, 9, 3, 8, 5, 2, 1],
    [1, 2, 8, 5, 7, 4, 6, 3, 9],
    [5, 7, 1, 8, 9, 2, 4, 6, 3],
    [8, 9, 6, 7, 4, 3, 1, 5, 2],
    [2, 4, 3, 6, 1, 5, 9, 8, 7]
])

sudoku_solved([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
])
