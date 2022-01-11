const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';

$.getJSON(URL, function (data) {
  const hi = data.hello;
  $('DIV#hello').text(hi);
});
