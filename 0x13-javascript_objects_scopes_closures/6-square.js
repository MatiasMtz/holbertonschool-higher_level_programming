#!/usr/bin/node
// class Square that defines a square and inherits from Rectangle
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let column = 0; column < this.height; column++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
