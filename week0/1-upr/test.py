from copy import copy, deepcopy

def matrix_bombing_plan(m):
    new_matrix = [row[:] for row in m]
    print(new_matrix)
    
matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]])