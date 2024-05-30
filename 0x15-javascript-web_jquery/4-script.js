// Ensure the DOM is fully loaded before running the script
$(document).ready(function () {
  // Attach a click event handler to the div with id "toggle_header"
  $('#toggle_header').click(function () {
    // Select the <header> element
    const header = $('header');
    
    // Toggle the class between 'red' and 'green'
    if (header.hasClass('red')) {
      header.removeClass('red').addClass('green');
    } else {
      header.removeClass('green').addClass('red');
    }
  });
});
