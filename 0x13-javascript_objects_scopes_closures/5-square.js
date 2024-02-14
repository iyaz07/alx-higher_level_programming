#!/usr/bin/node

// Creates a Square class that extends Rectangle class

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
