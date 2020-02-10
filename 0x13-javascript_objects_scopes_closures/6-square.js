#!/usr/bin/node
const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint (c) {
    let printChar = 'X';
    if (c) {
      printChar = c;
    }
    const arrayX = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        arrayX[j] = printChar;
      }
      console.log(arrayX.join(''));
    }
  }
}

module.exports = Square;
