#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, { encoding: 'utf-8' }, function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
