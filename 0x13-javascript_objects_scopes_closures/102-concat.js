#!/usr/bin/node
const fs = require('fs');

const sFile1 = process.argv[2];
const sFile2 = process.argv[3];
const dFile = process.argv[4];

const cont1 = fs.readFileSync(sFile1, 'utf-8');
const cont2 = fs.readFileSync(sFile2, 'utf-8');
const concatenatedCont = cont1 + cont2;

fs.writeFileSync(dFile, concatenatedCont);
