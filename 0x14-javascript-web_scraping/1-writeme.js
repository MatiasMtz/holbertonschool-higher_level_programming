#!/usr/bin/node
// script that writes a string to a file.
const fs = require('fs');
const args = process.argv.slice(2);

fs.writeFile(args[0], args[1], 'utf8', (error) => {
  if (error) {
    console.error(error);
  }
});
