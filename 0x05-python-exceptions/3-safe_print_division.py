#!/usr/bin/python3

def safe_print_division(a, b):
    """Division of a by b.

    Args:
        a: First number
        b: Second number

    Return:
        a / b
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
