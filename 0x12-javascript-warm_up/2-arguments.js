#!/usr/bin/node

const size = process.argv.length - 2;
if (size === 0) {
	  console.log('No argument');
} else if (size === 1) {
	  console.log('Argument found');
} else {
	  console.log('Arguments found');
}
