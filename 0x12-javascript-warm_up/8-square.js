#!/usr/bin/node

let x;
let y;
const Value = parseInt(process.argv[2]);

if (isNaN(Value)) {
  console.log('Missing size');
} else {
  for (x = 0; x < Value; x++) {
    let line = '';
    for (y = 0; y < Value; y++) {
      line += 'X';
    }
    console.log(line);
  }
}
