#!/usr/bin/python3

"""
Fetches the status of https://alx-intranet.hbtn.io/status using urllib.

This script sends a GET request to the provided URL using urllib.request.urlop
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
        body = response.read()
        utf8_content = body.decode('utf-8')
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", repr(body))
        print("\t- utf8 content:", utf8_content)
except urllib.error.URLError as e:
    print("Error fetching URL:", e)
