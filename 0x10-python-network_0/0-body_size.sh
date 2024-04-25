#!/bin/bash

# Script: 0-body_size.sh
# This script takes in a URL, sends a request to that URL, and displays the size of the body of the response in bytes.

# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url=$1

# Send a request to the URL using curl with silent mode and get the size of the response body
response=$(curl -s -w "%{size_download}" -o /dev/null "$url")

# Display the size of the response body in bytes
echo "$response"

