#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let count = 0; count < list.length; count++) {
    if (list[count] === searchElement) {
      counter += 1;
    }
  }
  return counter;
};
