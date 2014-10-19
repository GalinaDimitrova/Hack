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
        return False
    elif check_row(transposed) == False:
        return False
    elif check_square(sudoku) == False:
        return False
    else:
        return True
