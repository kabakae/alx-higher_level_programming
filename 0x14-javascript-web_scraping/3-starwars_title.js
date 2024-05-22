#!/usr/bin/node
/*
This script prints the title of a Star Wars movie where the episode number matches a given integer.
The first argument is the movie ID.
You must use the Star Wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id.
You must use the module request.
*/

const request = require('request');
const process = require('process');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  console.error('Usage: ./3-starwars_title.js <movie_id>');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
