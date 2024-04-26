#!/usr/bin/python3

"""
Sends a request to the provided URL and displays the value of the X-Request-Id variable found in the header of the response.

This script takes in a URL, sends a request using urllib.request.urlopen(), and displays the value of the X-Request-Id variable found in the header of the response.

Example:
    $ python3 script_name.py https://example.com
"""

import urllib.request
import sys

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

try:
    with urllib.request.urlopen(url) as response:
        request_id = response.headers.get('X-Request-Id')
        if request_id:
            print(request_id)
except urllib.error.URLError as e:
    print("Error fetching URL:", e)

