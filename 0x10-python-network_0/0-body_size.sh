#!/bin/bash

# Check if the URL is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a request to the URL using curl and get the size of the response body
response=$(curl -s -w "%{size_download}" -o /dev/null "$1")

# Display the size of the response body in bytes
echo "$response"
