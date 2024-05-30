// Ensure the DOM is fully loaded before running the script
$(document).ready(function () {
  // Fetch the character name from the API
  $.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    // Display the character name in the <div> with id "character"
    $('#character').text(data.name);
  });
});
