#!/usr/bin/node
const arg = 'C is fun';
const x = process.argv[2];
for (let i = 0; i < x; i++) {
  console.log(arg);
}
