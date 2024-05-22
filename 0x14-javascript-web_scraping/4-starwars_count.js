#!/usr/bin/node
/*
This script prints the number of movies where the character "Wedge Antilles" is present.
The first argument is the API URL of the Star Wars API: https://swapi-api.alx-tools.com/api/films/
Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
You must use the module request
*/

const request = require('request');
const process = require('process');

const apiUrl = process.argv[2];
const characterId = '18';

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }
  let films;
  try {
    films = JSON.parse(body).results;
  } catch (parseError) {
    console.error('Error: Failed to parse response body as JSON');
    return;
  }
  const filmsWithWedgeAntilles = films.filter(film =>
    film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
  );
  console.log(filmsWithWedgeAntilles.length);
});
