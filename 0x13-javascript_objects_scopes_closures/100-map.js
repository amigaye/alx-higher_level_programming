#!/usr/bin/node
const array= require('./100-data').list;

console.log(array);
let count = 0;
const map1 = array.map(function (x) {
  return (x * count++);
});

console.log(map1);
