#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(h) && Number.isInteger(w) && h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }
}
module.exports = Rectangle;
