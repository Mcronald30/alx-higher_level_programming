#!/usr/bin/node
const arg = process.argv[2];
const numb = factorial(arg);
function factorial (x) {
  if (isNaN(x)) {
    return (1);
  }

  x = parseInt(x);
  if (x <= 1) {
    return (1);
  } else {
    return (x * factorial(x - 1));
  }
}
console.log(numb);
