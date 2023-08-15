#!/usr/bin/node
const data = require('./100-data');

const currentList = data.list;
const newList = currentList.map((value, index) => value * index);

console.log(currentList);
console.log(newList);
