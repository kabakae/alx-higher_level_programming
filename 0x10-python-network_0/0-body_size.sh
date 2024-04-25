#!/bin/bash

# Check if URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send request and get the response body size in bytes
SIZE=$(curl -s "$URL" | wc -c)
if [ -z "$SIZE" ]; then
    echo "Error: Size of the response body could not be determined"
    exit 1
fi

echo "$SIZE"

