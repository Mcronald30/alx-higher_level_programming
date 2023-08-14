#!/usr/bin/node
const arg = process.argv[2];
const myNum = parseInt(arg);
if (!isNaN(myNum)) {
  console.log(`My number: ${myNum}`);
} else {
  console.log('Not a number');
}
