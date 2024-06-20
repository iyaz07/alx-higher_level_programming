#!/usr/bin/node

const SQ = require('./5-square');

class Square extends SQ {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let x;
    let y;
    for (x = 0; x < this.height; x++) {
      let line = '';
      for (y = 0; y < this.width; y++) {
        line += c;
      }
      console.log(line);
    }
  }
}

module.exports = Square;
