#!/usr/bin/node
// script that display the status code of a GET request
const axios = require('axios');
const args = process.argv.slice(2);

axios.get(args[0])
  .then(function (response) {
    console.log('code: ', response.status);
  })
  .catch(function (error) {
    console.log('code:', error.response.status);
  });
