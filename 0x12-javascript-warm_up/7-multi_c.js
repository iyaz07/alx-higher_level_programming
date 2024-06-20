#!/usr/bin/node

let i;
const Value = parseInt(process.argv[2]);
const loop = 'C is fun';

if (isNaN(Value)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < Value; i++) {
    console.log(loop);
  }
}
