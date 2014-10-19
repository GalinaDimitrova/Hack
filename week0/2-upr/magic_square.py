def sum_list(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    return result


def check_row_sum(row_sum, matrix):
    for i in range(1, len(matrix)):
        if row_sum != sum_list(matrix[i]):
            return False
    return True


def check_first_diagonal(matrix, row_sum):
    i, j = 0, 0
    diagonal_sum = 0
    while i != len(matrix[0]) and j != len(matrix[0]):
        diagonal_sum += matrix[i][j]
        i += 1
        j += 1
    if diagonal_sum != row_sum:
        return False
    return True


def check_second_diagonal(matrix, row_sum):
    i = 0
    j = len(matrix[0]) - 1
    diagonal_sum = 0
    while i != len(matrix[0]) and j != -1:
        diagonal_sum += matrix[i][j]
        i += 1
        j -= 1
    if diagonal_sum != row_sum:
        return False
    return True


def magic_square(matrix):
    # All sums should be equal to the sum of the first row
    row_sum = sum_list(matrix[0])
    transposed = []
    # check the basic matrix
    if check_row_sum(row_sum, matrix) == False:
        return False
        # transpose the matrix
    for i in range(len(matrix[0])):
        transposed.append([row[i] for row in matrix])

    if check_row_sum(row_sum, transposed) == False:
        return False
    # check first diagonal
    if check_first_diagonal(matrix, row_sum) == False:
        return False
    # check the other diagonal
    if check_second_diagonal(matrix, row_sum) == False:
        return False
    return True
