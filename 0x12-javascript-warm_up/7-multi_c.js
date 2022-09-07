#!/usr/bin/node

const process = require('process');

const n = parseInt(process.argv[2]);

if (isNaN(n)){
	console.log('Missing number of occurences');
} else if (! isNaN(n)){
for (let i = 0; i < n; i++) {
  console.log('C is fun');
}
}
