#!/usr/bin/node
/*
This script displays the status code of a GET request.
The first argument is the URL to request (GET).
The status code must be printed like this: code: <status code>.
You must use the module request.
*/

const request = require('request');
const process = require('process');

const url = process.argv[2];

if (!url) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  console.log('code:', response && response.statusCode);
});
