#!/usr/bin/node

const arg = process.argv.length - 1;

if (arg < 2) {
  console.log('No argument');
} else if (arg === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
