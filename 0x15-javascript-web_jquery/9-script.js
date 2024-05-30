// Fetch the translation of "hello" in French from the specified URL
$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  type: 'GET',
  success: function (response) {
    // Display the translation in the <div> with id "hello"
    $('#hello').text(response.hello);
  }
});
