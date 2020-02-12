#!/usr/bin/node

const request = require('request');
let requestDict = {};
request(process.argv[2], function (error, response, body) {
  if (!error) {
    requestDict = JSON.parse(response.body);
    const tasks = {};
    let userId = null;
    let totalTasks = 0;
    for (let i = 0; i < requestDict.length; i++) {
      if (userId !== requestDict[i].userId) {
        totalTasks = 0;
        userId = requestDict[i].userId;
      }
      if (requestDict[i].completed) {
        totalTasks++;
      }
      tasks[requestDict[i].userId] = totalTasks;
    }
    console.log(tasks);
  }
});
