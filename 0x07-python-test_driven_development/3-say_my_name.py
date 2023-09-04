#!/usr/bin/python3
"""Divide intergers in a matrix module with testing."""


def say_my_name(first_name, last_name=""):
    """Print first name and last name.

    Args:
        first_name (:obj:`str`): first name.
        last_name (:obj:`str`): last name.

    Raises:
            TypeError: first_name must be a string or
                    last_name must be a string.
    """
    if not first_name or not last_name:
        raise ValueError("first_name OR last_name cannot be empty.")
    if (not isinstance(first_name, str) or
            not isinstance(last_name, str)):
        raise TypeError(
            "first_name must be a string or last_name must be a string")
    print(f"My name is {first_name} {last_name}")
