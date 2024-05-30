// Ensure the DOM is fully loaded before running the script
$(document).ready(function () {
  // Fetch the movie data from the API
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    // Iterate over each movie in the data
    $.each(data.results, function (index, movie) {
      // Create a new <li> element with the movie title and append it to the <ul> with id "list_movies"
      $('<li>').text(movie.title).appendTo('#list_movies');
    });
  });
});
