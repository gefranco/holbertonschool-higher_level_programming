#!/usr/bin/node
if (parseInt(process.argv[2])) {
  const arrayXs = [];
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    for (let j = 0; j < parseInt(process.argv[2]); j++) {
      arrayXs[j] = 'X';
    }
    console.log(arrayXs.join(''));
  }
} else {
  console.log('Missing size');
}
