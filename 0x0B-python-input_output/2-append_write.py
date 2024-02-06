#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    Args:
        filename (str): name of file to append to.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        returns f.write(text)
