// script that fetches from https://fourtonfish.com/hellosalut/?lang=fr and displays the
// value of hello from that fetch in the HTML tag DIV#hello.
$('document').ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
