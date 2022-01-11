#!/usr/bin/node

const request = require('request');
const StarWarsURL = process.argv[2];
let count = 0;

request(StarWarsURL, function (_error, _response, body) {
  const parsedBody = JSON.parse(body).results;

  for (let i = 0; i < parsedBody.length; i++) {
    const characters = parsedBody[i].characters;

    for (let x = 0; x < characters.length; x++) {
      const char = characters[x];
      const charID = char.split('/')[5];

      if (charID === '18') {
        count += 1;
      }
    }
  }
  console.log(count);
});
