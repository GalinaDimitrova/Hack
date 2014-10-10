
def sum_list(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    return result


def sum_matrix(m):
    result = 0
    for i in range(len(m)):
        result += sum_list(m[i])
    return result


def check(x, y):
    if ((x < 0) or (y < 0) or (x >= row_count) or (y >= elements_count)):
        return False
    else:
        return True


def matrix_bombing_plan(m):
    row_count = len(m)
    elements_count = len(m[0])
    new_dict = {}
    # copy existing matrix into a new one
    new_matrix = [row[:] for row in m]
    for i in range(row_count):
        for j in range(elements_count):
            if i in range(row_count) and j + 1 in range(elements_count):
                new_matrix[i][j + 1] = m[i][j + 1] - m[i][j]
            if i in range(row_count) and j - 1 in range(elements_count):
                new_matrix[i][j - 1] = m[i][j - 1] - m[i][j]
            if i + 1 in range(row_count) and j in range(elements_count):
                new_matrix[i + 1][j] = m[i + 1][j] - m[i][j]
            if i - 1 in range(row_count) and j in range(elements_count):
                new_matrix[i - 1][j] = m[i - 1][j] - m[i][j]
            if i + 1 in range(row_count) and j + 1 in range(elements_count):
                new_matrix[i + 1][j + 1] = m[i + 1][j + 1] - m[i][j]
            if i + 1 in range(row_count) and j - 1 in range(elements_count):
                new_matrix[i + 1][j - 1] = m[i + 1][j - 1] - m[i][j]
            if i - 1 in range(row_count) and j + 1 in range(elements_count):
                new_matrix[i - 1][j + 1] = m[i - 1][j + 1] - m[i][j]
            if i - 1 in range(row_count) and j - 1 in range(elements_count):
                new_matrix[i - 1][j - 1] = m[i - 1][j - 1] - m[i][j]
            new_dict[(i, j)] = sum_matrix(new_matrix)
            new_matrix = [row[:] for row in m]
    # Sort the dictionary ????
    print(new_dict)
    return new_dict


matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
