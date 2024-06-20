#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    let j;
    for (i = 0; i < this.height; i++) {
      let line = '';
      for (j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }
}

module.exports = Rectangle;
