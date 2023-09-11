#!/usr/bin/python3
"""My list module file with python."""


class MyList(list):
    """My list Class that inherit  for list."""

    def print_sorted(self):
        """Print sorted list."""
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)


