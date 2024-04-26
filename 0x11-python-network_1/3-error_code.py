#!/usr/bin/python3

"""
Sends a request to the provided URL and displays the body of the response (de.

This script takes in a URL as a command-line argument. It then sends a request

Example:
    $ python3 script_name.py https://example.com
"""

import urllib.request
import urllib.error
import sys

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print(body)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
