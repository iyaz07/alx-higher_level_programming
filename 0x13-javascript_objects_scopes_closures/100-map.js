#!/usr/bin/node

const imported = require('./100-data').list;
const newlist = imported.map((x, i) => x * i);
console.log(imported);
console.log(newlist);
