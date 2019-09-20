#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if matrix is None:
        return
    j = 0
    matrix_copy = matrix[:]
    for i in matrix_copy:
        matrix_copy[j] = list(map(lambda x: x * x,  i))
        j += 1
    return matrix_copy
