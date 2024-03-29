#!/usr/bin/python3
# 6-from_json_string.py
"""Define a JSON-OBJECT function."""
import json


def from_json_string(my_str):
    """Returns python object representation of a JSON string."""
    return json.loads(my_str)
