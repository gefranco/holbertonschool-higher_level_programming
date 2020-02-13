#!/usr/bin/node

const request = require('request');
let requestDict = {};
let countCharacter = 0;

let url = null;
if (process.argv[2]) {
  url = process.argv[2];
}

request(url, function (error, response, body) {
  if (!error) {
    requestDict = JSON.parse(response.body);
    const results = requestDict.results;
    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j].includes('people/18/')) {
          countCharacter++;
        }
      }
    }
    console.log(countCharacter);
  }
});
