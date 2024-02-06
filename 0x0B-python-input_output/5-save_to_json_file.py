#!/usr/bin/python3
"""Define a Json file-writing functio."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to ale using JSON representation."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
