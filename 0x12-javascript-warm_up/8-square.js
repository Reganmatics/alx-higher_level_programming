#!/usr/bin/node

const process = require('process');

const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else if (!isNaN(size)) {
  const str = 'X';
  for (let i = 0; i < size; i++) {
    console.log(str.repeat(size));
  }
}
