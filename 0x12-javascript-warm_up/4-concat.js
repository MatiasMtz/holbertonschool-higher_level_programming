#!/usr/bin/node
// script that prints two arguments passed to it, in the following format: "is"
const { argv } = require('process');
let first;
let second;

if (argv[2] === undefined) {
  first = 'undefined';
} else {
  first = argv[2];
}
if (argv[3] === undefined) {
  second = 'undefined';
} else {
  second = argv[3];
}
console.log(`${first} is ${second}`);
