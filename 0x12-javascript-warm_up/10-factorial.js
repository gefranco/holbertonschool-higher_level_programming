#!/usr/bin/node
if (parseInt(process.argv[2])) {
  console.log(factorial(parseInt(process.argv[2])));
} else {
  console.log(1);
}
function factorial (n) {
  if (n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
