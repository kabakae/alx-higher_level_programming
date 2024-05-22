#!/usr/bin/node
/*
This script reads and prints the content of a file.
The first argument is the file path.
The content of the file must be read in UTF-8 encoding.
If an error occurs during reading, the error object is printed.
*/

const fs = require('fs');
const process = require('process');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: ./0-readme.js <file_path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
