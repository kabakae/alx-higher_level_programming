#!/usr/bin/node
/*
This script gets the contents of a webpage and stores it in a file.
The first argument is the URL to request.
The second argument is the file path to store the body response.
The file must be UTF-8 encoded.
You must use the module axios.
*/

const axios = require('axios');
const fs = require('fs');
const process = require('process');

const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  console.error('Usage: ./5-request_store.js <URL> <file_path>');
  process.exit(1);
}

axios.get(url)
  .then(response => {
    fs.writeFile(filePath, response.data, 'utf8', (err) => {
      if (err) {
        console.error('Error writing file:', err);
        return;
      }
      console.log(`File ${filePath} saved with contents from ${url}`);
    });
  })
  .catch(error => {
    if (error.response) {
      console.error(`Error: Status code ${error.response.status}`);
    } else {
      console.error('Error:', error.message);
    }
  });
