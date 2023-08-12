#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print elements in reversed order.

    Args:
        my_list: list of elements
    """
    for i in my_list[::-1]:
        print("{:d}".format(i))

