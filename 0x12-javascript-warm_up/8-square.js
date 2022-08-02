#!/usr/bin/node
// prints a square

const args = process.argv;
if (isNaN(Number(args[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < Number(args[2]); i++) {
    let square = '';
    for (let i = 0; i < Number(args[2]); i++) {
      square += 'X';
    }
    console.log(square);
  }
}
