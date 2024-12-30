#!/usr/bin/node

function factorial (n) {
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const input = process.argv[2];
const num = parseInt(input, 10);
console.log(factorial(num));
