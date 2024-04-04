$(document).ready(function() {
  $('div#add_item').click(function() {
    $('ul.my_list').append('<li>Item</li>')
  });
  $('div#remove_item').click(function() {
    let list = $('ul.my_list li');
    if (list.length > 0) {
      list[list.length - 1].remove();
    }
  });
  $('div#clear_list').click(function() {
    $('ul.my_list li').remove();
  });
});
