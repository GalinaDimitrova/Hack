def sum_list(lst):
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    return result


def sum_matrix(m):
    result = 0
    for i in range(len(m)):
        result += sum_list(m[i])
    print(result)
    return result

sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
