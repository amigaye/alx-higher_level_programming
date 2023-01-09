#!/usr/bin/node
// Script imports a dictionary of occurrences by user id
// and computes a dictionary of user ids by occurrence.

const { dict } = require('./101-data.js');
const newDict = {};
for (const N in dict) {
  if (newDict[dict[N]] === undefined) {
    newDict[dict[N]] = [];
  }
  newDict[dict[N]].push(N);
}

console.log(newDict);
