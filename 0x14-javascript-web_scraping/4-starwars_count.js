#!/usr/bin/node
// script that prints the title of a Star Wars movie
const axios = require('axios');
const args = process.argv.slice(2);
let appearances = 0;

axios.get(args[0])
  .then(response => {
    const films = response.data.results ? response.data.results : [];
    const size = films.length;
    for (let count = 0; count < size; count++) {
      films[count].characters.forEach(character => {
        if (character.includes('18')) {
          appearances += 1;
        }
      });
    }
    console.log(appearances);
  })
  .catch(error => {
    console.log('Error:', error);
  });
