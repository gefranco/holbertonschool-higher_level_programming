#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let biggest = process.argv[2];
  let secondBiggest = process.argv[2];
  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > biggest) {
      biggest = parseInt(process.argv[i]);
    }
  }

  for (let i = 2; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > secondBiggest && parseInt(process.argv[i]) < biggest) {
      secondBiggest = parseInt(process.argv[i]);
    }
  }
  console.log(secondBiggest);
}
