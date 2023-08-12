#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print matrix function.

    Args:
                matrix: matrix to print
    """
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end=" " if col != row[-1] else "")
        print()
