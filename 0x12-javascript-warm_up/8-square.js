#!/usr/bin/node
const mySqu = process.argv[2];
if (isNaN(mySqu)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < mySqu; x++) {
    console.log('X'.repeat(mySqu));
  }
}
