#!/usr/bin/node
// script that prints the title of a Star Wars movie
const axios = require('axios');
const args = process.argv.slice(2);
const api = 'https://swapi-api.hbtn.io/api/films/';

axios.get(api.concat(args[0]))
  .then(response => {
    console.log(response.data.title);
  });
