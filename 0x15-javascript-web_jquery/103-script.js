$(document).ready(function () {
  // Add event listener to Translate button and Enter key press
  $('#btn_translate, #language_code').on('click keypress', function (event) {
    // Check if the click event or the Enter key press occurred
    if (event.type === 'click' || event.key === 'Enter') {
      // Fetch the language code provided by the user
      const languageCode = $('#language_code').val();

      // Fetch the translation from the API
      fetchTranslation(languageCode);
    }
  });

  // Function to fetch translation from the API
  function fetchTranslation(languageCode) {
    const url = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;
    
    // Fetch data from the API
    $.getJSON(url)
      .done(function (data) {
        // Display the translation in the <div> element with id "hello"
        $('#hello').text(data.hello);
      })
      .fail(function (jqxhr, textStatus, error) {
        // Handle errors
        console.error('Error fetching translation:', error);
        $('#hello').text('Error: Translation not found');
      });
  }
});
