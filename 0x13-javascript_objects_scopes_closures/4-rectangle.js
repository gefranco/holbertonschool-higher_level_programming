#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(h) && Number.isInteger(w) && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const arrayX = [];
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        arrayX[j] = 'X';
      }
      console.log(arrayX.join(''));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
