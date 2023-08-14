#!/usr/bin/node
const myObj = {
  type: 'object',
  value: 12,
  incr: function() {
    this.value += 1;
  }
};

console.log(myObj);

myObj.incr();
console.log(myObj);

myObj.incr();
console.log(myObj);

myObj.incr();
console.log(myObj);
