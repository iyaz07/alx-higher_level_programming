#!/usr/bin/node
// This is a script that prints the title of a Star Wars
// movie where the episode number matches a given integer.

const request = require('request');
const fs = require('fs');
const cmd = process.argv.slice(2);
const url = cmd[0];
const filename = cmd[1];
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const cont = body;
    fs.writeFile(filename, cont, (err) => {
      if (err) console.log(err);
    });
  }
});
