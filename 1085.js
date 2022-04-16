const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ');

console.log(
  Math.min(
    Number(input[0]),
    Number(input[1]),
    Number(input[2]) - Number(input[0]),
    Number(input[3]) - Number(input[1])
  )
);
