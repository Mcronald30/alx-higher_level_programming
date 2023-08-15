#!/usr/bin/node
const data = require('./101-data');

const Dict = data.dict;
const newDict = {};

for (const userId in Dict) {
  const occurrences = Dict[userId];

  if (!(occurrences in newDict)) {
    newDict[occurrences] = [];
  }

  newDict[occurrences].push(userId);
}

console.log(newDict);
