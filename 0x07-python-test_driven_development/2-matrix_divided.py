#!/usr/bin/python3
"""
Module Divide Matrix
    """


def matrix_divided(matrix, div):
    """
        Divides all elements in matrix

        Args:
            matrix (list[list[int/float]]) : matrix
            div (int/float) Devider
        Raise:
            TypeError: div not int or float
            TypeError: matrix is not a list of list of number
            ZeroDivisionError: Div is 0
        Return : New matrix Divided
        
        """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if (
        type(matrix) is not list
        or any(type(l) is not list for l in matrix)
        or not all((isinstance(n, (int, float)) for n in l) for l in matrix)
        or len(matrix[0]) == 0
    ):
        raise TypeError(
                "matrix must be a matrix "
                "(list of lists) of integers/floats")
