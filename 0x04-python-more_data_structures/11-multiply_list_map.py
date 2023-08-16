#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """Multiply each number in a list.

    Args:
        my_list: list[]
        number: Number to multiply each number with

    Returns:
            New list []
    """
    return (list(map((lambda i: i * number), my_list)))
