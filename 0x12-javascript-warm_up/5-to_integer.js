#!/usr/bin/node

const Value = parseInt(process.argv[2]);

if (isNaN(Value)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Value}`);
}
