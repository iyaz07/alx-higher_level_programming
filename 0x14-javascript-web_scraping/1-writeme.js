#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];
const InfoToWrite = process.argv[3];

fs.writeFile(filePath, InfoToWrite, 'utf-8', (err) => {
  if (err) {
    console.error('Error occurred:', err);
  }
});
