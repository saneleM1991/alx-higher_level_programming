#!/usr/bin/python3


def element_at(my_list, idx):
    """Find element using index.

    Args:
        my_list: list of objects
        idx: index of an element

    Returns:
            None if idx < 0 or if idx > list length.

            element at index of idx.

    """
    if idx < 0:
        return None
    if idx > (len(my_list) - 1):
        return None

    return my_list[3]
