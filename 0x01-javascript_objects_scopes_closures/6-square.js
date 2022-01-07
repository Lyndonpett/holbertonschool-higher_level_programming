#!/usr/bin/node

const SquareOG = require('./5-square');

class Square extends SquareOG {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log('C'.repeat(this.width));
    }
  }
}
module.exports = Square;
