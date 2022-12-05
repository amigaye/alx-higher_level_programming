#!/usr/bin/node
if (process.argv.length < 3) {
  console.log(undefined + ' is ' + undefined);
}
else if (process.argv.length == 3) {
  console.log(process.argv[2] + ' is ' + undefined)
} else {
  console.log(process.argv[2] + ' is ' + process.argv[3]);
}
