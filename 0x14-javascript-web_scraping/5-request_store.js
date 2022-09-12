#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.
const axios = require('axios');
const fs = require('fs');
const args = process.argv.slice(2);

axios.get(args[0])
  .then(response => {
    fs.writeFile(process.argv[3], response.data, error => {
      if (error) {
        console.error(error);
      }
    });
  });
