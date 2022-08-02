#!/usr/bin/node
// class Rectangle that defines a rectangle
class Rectangle {
	constructor(w, h) {
		if (w > 0 && h > 0) {
			this.width = w;
			this.height = h;
		}
	}
	print() {
		for (let column = 0; column < this.height; column++) {
			console.log('X'.repeat(this.width));
		}
	}
}

module.exports = Rectangle;
