#!/usr/bin/node
// prints 3 lines using an array of string and a loop

const args = process.argv;
if (isNaN(Number(args[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < Number(args[2]); i++) {
    console.log('C is fun');
  }
}
