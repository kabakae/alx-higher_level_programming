#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of UF8 TO STDOUT."""
    with open(filename, encodin"utf-8") as f:
        print(f.read(), end="")