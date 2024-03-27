#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
const ID = 'https://swapi-api.alx-tools.com/api/people/18/';

request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error occurred:', error);
  } else {
    if (response.statusCode === 200) {
      const movies = JSON.parse(body).results;
      const Films = movies.filter(movie => movie.characters.includes(ID));
      console.log(`${Films.length}`);
    } else {
      console.error('Error occurred:', error);
    }
  }
});
