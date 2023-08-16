#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Square each number in a matrix.

    Args:
        matrix: matrix to square

    Returns:
            new squared matrix without
            modifeing old matrix
    """
    new_matrix = list(map(lambda items: [i * i for i in items], matrix))
    return new_matrix
