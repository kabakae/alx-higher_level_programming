#!/usr/bin/node
/*
This script computes the number of tasks completed by user ID.
The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
Only users with completed tasks are printed.
You must use the module request.
*/

const request = require('request');
const process = require('process');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API_URL>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
    return;
  }
  const tasks = JSON.parse(body);
  const completedTasks = tasks.filter(task => task.completed === true);
  const completedTasksByUser = completedTasks.reduce((acc, task) => {
    acc[task.userId] = acc[task.userId] ? acc[task.userId] + 1 : 1;
    return acc;
  }, {});
  console.log(completedTasksByUser);
});
