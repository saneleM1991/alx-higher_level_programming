#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Add uniq int in alist.

    Args:
                my_list: List of intergers

    Return:
                Sum of uniq intergers
    """
    uniq_int = set(my_list)
    sum_of_uniq_int = 0
    for i in uniq_int:
        sum_of_uniq_int += i
    return sum_of_uniq_int
