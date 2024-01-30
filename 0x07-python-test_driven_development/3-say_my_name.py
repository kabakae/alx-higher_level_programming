#!/usr/bin/python3


"""Define a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.
    Args:
    first_name (str): The first name to point.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be astring")
    print("My name is {}{}".format(first_name, last_name))
