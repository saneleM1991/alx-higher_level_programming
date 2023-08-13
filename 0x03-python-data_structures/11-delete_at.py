#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list.

    Args:
        my_list: list[] of numbers
        idx: index of an item in list

    Returns:
                Modifide list
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
