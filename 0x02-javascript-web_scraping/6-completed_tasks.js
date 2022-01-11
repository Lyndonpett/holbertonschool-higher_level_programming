#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response.statusCode === 200) {
    const finished = {};
    for (const task of JSON.parse(body)) {
      if (task.completed === true) {
        if (task.userId in finished) {
          finished[task.userId] += 1;
        } else {
          finished[task.userId] = 1;
        }
      }
    }
    console.log(finished);
  }
});
