#!/usr/bin/node
// script that concats 2 files
const fileSystem = require('fs');
const argv = require('process').argv;

fileSystem.readFile(argv[2], 'utf8', function (err, data) {
  if (err) throw err;
  fileSystem.writeFile(argv[4], data, function (err) {
    if (err) throw err;
  });
});

fileSystem.readFile(argv[3], 'utf8', function (err, data) {
  if (err) throw err;
  fileSystem.appendFile(argv[4], data, function (err) {
    if (err) throw err;
  });
});
