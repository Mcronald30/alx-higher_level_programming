#!/usr/bin/node
const args = process.argv.slice(2);
const integers = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));
integers.sort((a, b) => b - a);
if (integers.length < 2) {
  console.log(0);
} else {
  console.log(integers[1]);
}
