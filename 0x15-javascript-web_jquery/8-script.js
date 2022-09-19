// script that fetches and lists the title for all movies by using this URL:
// https://swapi-api.hbtn.io/api/films/?format=json
$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (_index, value) {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});
