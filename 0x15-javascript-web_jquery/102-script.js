$(document).ready(function () {
  // Add event listener to the Translate button
  $('#btn_translate').click(function () {
    // Fetch the language code provided by the user
    const languageCode = $('#language_code').val();

    // Fetch the translation from the API
    fetchTranslation(languageCode);
  });

  // Function to fetch translation from the API
  function fetchTranslation(languageCode) {
    const url = `https://fourtonfish.com/hellosalut/?lang=${languageCode}`;
    
    // Fetch data from the API
    fetch(url)
      .then(response => response.json())
      .then(data => {
        // Display the translation in the <div> element with id "hello"
        $('#hello').text(data.hello);
      })
      .catch(error => {
        // Handle errors
        console.error('Error fetching translation:', error);
        $('#hello').text('Error: Translation not found');
      });
  }
});
