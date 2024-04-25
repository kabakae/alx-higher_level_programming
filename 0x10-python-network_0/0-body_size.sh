#!/bin/bash

# Check if URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send request and get the response body
RESPONSE=$(curl -sI "$URL")
STATUS_CODE=$(echo "$RESPONSE" | head -n 1 | awk '{print $2}')

# Check if the request was successful (status code 200)
if [ -z "$STATUS_CODE" ]; then
    echo "Error: No response received"
    exit 1
elif [ "$STATUS_CODE" != "200" ]; then
    echo "Error: Request failed with status code $STATUS_CODE"
    exit 1
fi

# Extract size from response headers
SIZE=$(echo "$RESPONSE" | awk '/Content-Length/ {print $2}')
if [ -z "$SIZE" ]; then
    echo "Error: Content-Length not found in the response headers"
    exit 1
fi

echo "$SIZE"

