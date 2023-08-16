#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Multiply each valu in a dictionary by 2.

    Args:
                a_dictionary: Dictionary

    Returns:
                New modified dictionary
    """
    new_dir = a_dictionary.copy()
    list_keys = list(new_dir.keys())

    for i in list_keys:
        new_dir[i] *= 2

    return (new_dir)
