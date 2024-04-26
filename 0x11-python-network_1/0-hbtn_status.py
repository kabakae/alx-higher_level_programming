#!/usr/bin/python3

"""
Fetches the status of https://alx-intranet.hbtn.io/status using urllib.

This script sends a GET request to the provided URL using urllib.request.n().
It then reads the response body and prints it out with specified formatting.

Example:
    $ python3 script_name.py

Attributes:
    url (str): The URL to fetch the status from.
"""

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        response_info = response.info()
        print("- Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("- Headers:")
        for key in response_info.keys():
            print("\t- {}: {}".format(key, response_info.get(key)))
except urllib.error.URLError as e:
    print("Error fetching URL:", e)
