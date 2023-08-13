#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.

    Args:
                my_list: list of numbers

    Returns:
                list[] of multiples of twoo
    """
    multiples_of_twoo = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples_of_twoo.append(True)
        else:
            multiples_of_twoo.append(False)

    return (multiples_of_twoo)
