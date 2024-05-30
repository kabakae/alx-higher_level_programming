// Ensure the DOM is fully loaded before running the script
$(document).ready(function () {
  // Attach a click event handler to the div with id "update_header"
  $('#update_header').click(function () {
    // Update the text of the <header> element to "New Header!!!"
    $('header').text('New Header!!!');
  });
});
