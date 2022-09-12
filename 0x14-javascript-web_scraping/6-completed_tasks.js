#!/usr/bin/node
// This script computes the number of tasks completed by user id.
const axios = require('axios');
const args = process.argv.slice(2);

axios.get(args[0])
  .then(response => {
    const obj = {};
    response.data.forEach(data => {
      if (data.completed === true) {
        if (obj[data.userId] === undefined) {
          obj[data.userId] = 1;
        } else {
          obj[data.userId]++;
        }
      }
    });
    console.log(obj);
  })
  .catch(err => {
    console.error('Error:', err);
  });
