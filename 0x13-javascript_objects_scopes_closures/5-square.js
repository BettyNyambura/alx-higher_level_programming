#!/usr/bin/node
// A class Square that defines a square and inherits from Rectangle

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the constructor of Rectangle with size for both width and height
  }
}

module.exports = Square;
