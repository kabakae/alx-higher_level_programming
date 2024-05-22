#!/usr/bin/node
/*
This script writes a string to a file.
The first argument is the file path.
The second argument is the string to write.
The content of the file must be written in UTF-8 encoding.
If an error occurs during writing, the error object is printed.
*/

const fs = require('fs');
const process = require('process');

const filePath = process.argv[2];
const fileContent = process.argv[3];

if (!filePath || !fileContent) {
  console.error('Usage: ./1-writeme.js <file_path> <file_content>');
  process.exit(1);
}

fs.writeFile(filePath, fileContent, 'utf8', (err) => {
  if (err) {
    console.error(err);
    return;
  }
});
