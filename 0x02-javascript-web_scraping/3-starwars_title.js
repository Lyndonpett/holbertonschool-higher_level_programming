#!/usr/bin/node

const request = require('request');
const StarWarsURL = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(StarWarsURL, function (_error, _response, body) {
  const parsedBody = JSON.parse(body);
  console.log(parsedBody.title);
});
