#!/usr/bin/node
/*
This script prints all characters of a Star Wars movie.
The first argument is the Movie ID - example: 3 = "Return of the Jedi"
Display one character name by line in the same order of the list "characters" in the /films/ response.
You must use the Star Wars API.
You must use the module request.
*/

const request = require('request');
const process = require('process');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

if (!movieId) {
  console.error('Usage: ./101-starwars_characters.js <movie_id>');
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
  const movieData = JSON.parse(body);
  const charactersUrls = movieData.characters;
  let charactersCount = 0;

  charactersUrls.forEach(characterUrl => {
    request(characterUrl, (err, res, charBody) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      if (res.statusCode !== 200) {
        console.error(`Error: Status code ${res.statusCode}`);
        return;
      }
      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
      charactersCount++;
      if (charactersCount === charactersUrls.length) {
        // All characters printed
        process.exit(0);
      }
    });
  });
});
