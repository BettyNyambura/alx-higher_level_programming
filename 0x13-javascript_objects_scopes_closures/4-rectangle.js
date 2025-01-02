#!/usr/bin/node
// A class Rectangle that defines a rectangle with various methods

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Method to print the rectangle using the character 'X'
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Method to swap the width and height of the rectangle
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  // Method to double the width and height of the rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
