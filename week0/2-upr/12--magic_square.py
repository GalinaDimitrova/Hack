def sum_list(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    return result


def check_row_sum(row_sum, matrix):
    for i in range(1, len(matrix)):
        if row_sum != sum_list(matrix[i]):
            return False


def magic_square(matrix):
    # All sums should be equal to the sum of the first row
    row_sum = sum_list(matrix[0])
    transposed = []
    # check the basic matrix
    if check_row_sum(row_sum, matrix) == False:
        print(False)
        return False
        # transpose the matrix
    for i in range(len(matrix[0])):
        transposed.append([row[i] for row in matrix])
    if check_row_sum(row_sum, transposed) == False:
        print(False)
        return False
    # check first diagonal
    i, j = 0, 0
    diagonal_sum = 0
    while i != len(matrix[0]) and j != len(matrix[0]):
        diagonal_sum += matrix[i][j]
        i += 1
        j += 1
    if diagonal_sum != row_sum:
        print(False)
        return False
    # check tho eother diagonal
    i = 0
    j = len(matrix[0]) - 1
    diagonal_sum = 0
    while i != len(matrix[0]) and j != -1:
        diagonal_sum += matrix[i][j]
        i += 1
        j -= 1
    if diagonal_sum != row_sum:
        print(False)
        return False
    print(True)
    return True


magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]])
magic_square([[7, 12, 1, 14], [2, 13, 8, 11], [16, 3, 10, 5], [9, 6, 15, 4]])
magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]])
magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]])
