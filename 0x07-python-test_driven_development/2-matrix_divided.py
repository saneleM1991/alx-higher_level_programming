#!/usr/bin/python3
"""Divide intergers in a matrix module with testing."""


def matrix_divided(matrix, div):
    """Divide all numbers in a matrix.

    Args:
            matrix ([[]]): numbers matrix.
            div (:obj:`int`): Divisor.

    Returns:
            [[]]New matrix.

    Raises:
            TypeError: matrix must be a matrix (list of lists) of
                               integers/floats OR Each row of the matrix must
                               have the same size OR div must be a number.
            ZeroDivisionError: if `div` is 0
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    else:
        for items in matrix:
            if not isinstance(items, list):
                raise TypeError(
                    "matrix must be a matrix (list of lists)" +
                    "of integers/floats")
            else:
                for item in items:
                    check_int_or_float(item)
        for items in matrix:
            check_row_size(matrix, items)
    return [[round(x / div, 2) for x in i] for i in matrix]


def check_int_or_float(item):
    """Chech if is int or float.
    Args:
        item: item to check.

    Raises:
        TypeError: matrix must be a matrix (list of lists) of
                   integers/floats
    """
    if (not isinstance(item, int)
            and not isinstance(item, float)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")


def check_row_size(matrix, items):
    """Check row size of each list inside matrix.

    Args:
        matrix: matrix.
        items: items

    Raises:
        TypeError: matrix must be a matrix (list of lists) of
                   integers/floats
    """
    row_size = len(matrix[0])
    if row_size != len(items):
        raise TypeError(
            "Each row of the matrix must have the same size")
