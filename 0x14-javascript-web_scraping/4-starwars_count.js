#!/usr/bin/node

const args = process.argv;
const url = args[2];
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const parsedBody = JSON.parse(body);
    const results = parsedBody.results;
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const chars = (results[i].characters);
      for (let j = 0; j < chars.length; j++) {
        const check18 = chars[j].endsWith('18/');
        if (check18) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
