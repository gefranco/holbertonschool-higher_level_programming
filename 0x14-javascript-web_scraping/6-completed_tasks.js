#!/usr/bin/node

const request = require('request');
let requestDict = {};
request(process.argv[2], function (error, response, body) {
  if (!error) {
    requestDict = JSON.parse(response.body);
    const tasks = {};
    for (let i = 0; i < requestDict.length; i++) {
      if (requestDict[i].completed) {
        if (!tasks[requestDict[i].userId]) {
          tasks[requestDict[i].userId] = 0;
        }
        tasks[requestDict[i].userId] += 1;
      }
    }
    console.log(tasks);
  }
});
