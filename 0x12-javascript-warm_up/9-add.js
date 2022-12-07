#!/usr/bin/node
const x = add(process.argv[2], process.argv[3]);
console.log(x);
function add (a, b) {
  return parseInt(a) + parseInt(b);
}
