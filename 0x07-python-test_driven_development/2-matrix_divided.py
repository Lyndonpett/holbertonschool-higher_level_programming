#!/usr/bin/python3
"""This module divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divides elements in a matrix by 2 decimal points"""

    errormessage = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(errormessage)

    for row in matrix:
        if type(row) is not list:
            raise TypeError(errormessage)
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(errormessage)

    rowLength = len(matrix[0])
    for row in matrix:
        if len(row) != rowLength:
            raise TypeError("Each row of the matrix must have the same size")

    # Handles div
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(number / div, 2) for number in list] for list in matrix]
