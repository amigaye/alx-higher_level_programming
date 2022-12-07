#!/usr/bin/node
function factorialize (num) {
  // If the number is less than 0, reject it.
  if (isNaN(num)) {
    return 1;
  } else if (num === 0) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}
console.log(factorialize(parseInt(process.argv[2])));
