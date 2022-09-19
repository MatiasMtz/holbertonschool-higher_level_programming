// script that toggles the class of the <header> element when
// the user clicks on the tag DIV#toggle_header:
$('DIV#toggle_header').click(function () {
  const color = $('header').hasClass('red');
  if (!color) {
    $('header').toggleClass('red');
  } else {
    $('header').toggleClass('green');
  }
});
