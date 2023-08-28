#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list.

    Args:
        my_list: list[] of elements
        x: Number of elements to be printed

    Returns:
            Number of elements printed
    """
    num_of_ele_printed = 0
    try:
        for index in range(x):
            print(f"{my_list[index]}", end="")
            num_of_ele_printed += 1
    except IndexError:
        pass
    print("")
    return num_of_ele_printed
