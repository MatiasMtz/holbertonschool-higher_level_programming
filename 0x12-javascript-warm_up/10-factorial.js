#!/usr/bin/node
// computes and prints a factorial

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
const args = process.argv;
const n = Number(args[2]);
if (isNaN(n)) {
  console.log(1);
} else {
  const fact = factorial(n);
  console.log(fact);
}
