#!/usr/bin/node
// script that reads and prints the content of a file.
const fs = require('fs');
const args = process.argv.slice(2);

fs.readFile(args[0], 'utf8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
