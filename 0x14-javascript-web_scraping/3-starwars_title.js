#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];
const URL = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request.get(URL, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
  } else {
    if (response.statusCode === 200) {
      const movieINFO = JSON.parse(body);
      console.log(`${movieINFO.title}`);
    } else {
      console.error('Error occurred:', error);
    }
  }
});
