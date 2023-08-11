#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """Replace element at specific index.

    Args:
        my_list: list of elements
        idx: index of an element
        elements: a replaycer element

    Return:
        Original list if idx < 0 or idx is out of range

        Modifide list
    """
    if idx < 0:
        return my_list
    if idx > (len(my_list) - 1):
        return my_list
    my_list[idx] = element
    return my_list
