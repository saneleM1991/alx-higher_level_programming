#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """replaces an element in a list at a specific
        position without modifying the original list.

    Args:
        my_list: list of elements
        idx: index of an element in alist
        element: element in alist

    Return:
        Copy of original list if idx < 0 or idx is out of range.

        Modifide copy of original list.
    """
    my_list_copy = my_list[:]
    if idx < 0:
        return my_list_copy
    if idx > (len(my_list) - 1):
        return my_list_copy
    my_list_copy[idx] = element
    return my_list_copy
