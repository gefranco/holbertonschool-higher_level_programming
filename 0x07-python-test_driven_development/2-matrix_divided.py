#!/usr/bin/python3
"""
"2-matrix_divide" module.

The 2-matrix_divide module supplies the function  matrix_divided(matrix, div):
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    matriz_result = []
    row_result = []
    row_length = len(matrix[0])
    for row in matrix:
        if row_length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        row_result = []
        for element in row:
            if not isinstance(element, (int, float)):
                msg = "matrix must be a matrix (list of lists)"
                msg += " of integers/floats"
                raise TypeError(msg)
            row_result.append(round((element / div), 2))
        matriz_result.append(row_result)
    return matriz_result
