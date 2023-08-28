#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer with "{:d}".format().

    Args:
                value: An integer to print

    Return:
                True if value is integer | False
    """
    try:
        int_value = int(value)
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
