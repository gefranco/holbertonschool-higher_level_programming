#!/usr/bin/node

const request = require('request');
let requestDict = {};
request('http://swapi.co/api/films/' + process.argv[2], function (error, response, body) {
  if (!error) {
    requestDict = JSON.parse(response.body);
    console.log(requestDict.title);
  }
});
