const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.getJSON(URL, function (data) {
  const name = data.name;
  $('DIV#character').text(name);
});
