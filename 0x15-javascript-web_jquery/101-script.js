// Add a new item to the list
$('#add_item').click(function () {
  $('<li>').text('Item').appendTo('ul.my_list');
});

// Remove the last item from the list
$('#remove_item').click(function () {
  $('ul.my_list li:last-child').remove();
});

// Clear all items from the list
$('#clear_list').click(function () {
  $('ul.my_list').empty();
});
