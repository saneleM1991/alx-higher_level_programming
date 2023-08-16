#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """Find defferent elements in twoo sets.

    Args:
        set_1: Set 1
        set_2: Ste 2

    Returns:
            New with element that a not common
    """
    return set_1 ^ set_2
