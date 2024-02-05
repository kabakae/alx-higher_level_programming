#!/usr/bin/python3
"""Defines an inherited list class Mylist."""


class MyList(list):
    """Implements sorted printing."""
    def print_sorted(self):
        """Print a list in sorted."""
        print(sorted(self))
