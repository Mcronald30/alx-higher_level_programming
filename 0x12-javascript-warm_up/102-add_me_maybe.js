#!/usr/bin/node
exports.addMeMaybe = function (numb, theFunction) {
  numb += 1;
  theFunction(numb);
};
