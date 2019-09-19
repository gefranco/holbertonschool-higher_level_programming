#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    if matrix is not None:
        my_matrix = matrix[:]
        for row in range(len(my_matrix)):
            my_matrix[row] = matrix[row][:]
            for i in range(len(my_matrix[row])):
                my_matrix[row][i] = my_matrix[row][i]**2

    return my_matrix
