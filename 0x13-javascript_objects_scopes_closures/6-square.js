#!/usr/bin/node
// A class Square that defines a square and inherits from the Square in 5-square.js

const SquareBase = require('./5-square');

class Square extends SquareBase {
  // Method to print the square using the specified character or 'X' if undefined
  charPrint (c) {
    const char = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(char.repeat(this.width));
    }
  }
}

module.exports = Square;
