#!/usr/bin/python3

"""
Sends a POST request to the provided URL with the email as a parameter and dis

This script takes in a URL and an email as commanutf-8.

Example:
    $ python3 script_name.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
"""

import urllib.request
import urllib.parse
import sys

if len(sys.argv) != 3:
    print("Usage: {} <URL> <email>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = urllib.parse.urlencode({'email': email}).encode('utf-8')

try:
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print("Your email is:", body)
except urllib.error.URLError as e:
    print("Error fetching URL:", e)
