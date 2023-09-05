#!/usr/bin/python3
"""Square module with test file."""


def print_square(size):
    """Printi square base on `size`.

    Args:
            size (`int`): length of the square.

    Raises:
            TypeError: if `size` not an `int` OR if
                               is `float` and < 0.
            ValueError: if `size` < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
