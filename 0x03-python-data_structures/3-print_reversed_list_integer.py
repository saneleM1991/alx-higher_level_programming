#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Print elements in reversed order.

    Args:
        my_list: list of elements
    """
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
