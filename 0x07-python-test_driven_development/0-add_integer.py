#!/usr/bin/python3
"""Add intergers module with testing."""


def add_integer(a, b=98):
    """Adding twoo intergers and return result.

    Args:
        a (:obj:`int`): first number
        b (:obj:`int` | :obj:`float`, optional): second number.

    Returns:
            `int` `a` + `b`

    Raises:
        TypeError: if both `a` and `b` are not an `int`.
    """
    if (not isinstance(a, int) and not isinstance(a, float) or
            not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
