#!/usr/bin/node

class Rectangle {
	construcotr(w, h) {
		if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) { return; }
	}

	print() {
		for (let i = 1; i < this.height; i++) {
			for (let j = 1; j < this.width; j++) {
				if (i != this.height){
					console.log('X' * this.width + '\n');
				} else if (i === this.height) {
					console.log('X' * this.width);
				}
			}
		}
	}
}

module.exports = Rectangle;
