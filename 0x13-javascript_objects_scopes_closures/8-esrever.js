#!/usr/bin/node
// function that returns the reversed version of a list
exports.esrever = function (list) {
  let end = list.length;
  let start = 0;
  const newList = [];
  for (start = 0; start < list.length; start++) {
    newList[start] = list[end - 1];
    end--;
  }
  return newList;
};
