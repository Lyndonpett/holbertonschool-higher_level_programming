#!/usr/bin/node

const num = process.argv.splice(2);

if (num.length === 0 || num.length === 1) {
  console.log(0);
} else {
  let i = 0;
  let max = 0;
  let result = 0;

  if (parseInt(num[0]) > parseInt(num[1])) {
    max = num[0];
    result = num[1];
  } else {
    max = num[1];
    result = num[0];
  }
  for (i = 2; i < num.length; i++) {
    if (parseInt(num[i]) >= parseInt(max)) {
      result = max;
      max = num[i];
    } else if (parseInt(num[i]) >= parseInt(result)) {
      result = num[i];
    }
  }
  console.log(result);
}
