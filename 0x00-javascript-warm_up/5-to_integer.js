#!/usr/bin/node

if (parseInt(process.argv[2])) {
  console.log('My number is: ' + parseInt(process.argv[2]));
} else {
  console.log('Not a number');
}
