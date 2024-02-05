#!/usr/bin/python3
"""Define a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly.
    Ars:
    obj (any)
    Returns:
    otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
