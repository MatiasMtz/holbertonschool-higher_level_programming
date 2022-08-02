#!/usr/bin/node
// script that imports an array and computes a new array
const list = require('./100-data').list;
const newList = list.map(function (number, index) {
  return (number * index);
});
console.log(list);
console.log(newList);
