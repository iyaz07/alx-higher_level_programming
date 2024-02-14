#!/usr/bin/node

// Print function with custom characters to represent the Square

const oldSquare = require('./5-square.js');

class Square extends oldSqaure {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    } else if (c === undefined) {
      for (let j = 0; j < this.height; j++) {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
