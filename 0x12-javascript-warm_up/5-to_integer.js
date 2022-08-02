#!/usr/bin/node
// script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer
const { argv } = require('process');

const num = parseInt(argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
