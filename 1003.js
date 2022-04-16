const [count, ...input] = require('fs')
  .readFileSync('/dev/stdin')
  .toString()
  .trim()
  .split('\n')
  .map(Number);
const arr = [];
for (let i = 0; i <= 39; i++) {
  if (i === 0) arr.push([1, 0]);
  else if (i === 1) arr.push([0, 1]);
  else arr.push([arr[i - 1][0] + arr[i - 2][0], arr[i - 1][1] + arr[i - 2][1]]);
}

input.forEach((n, i) => {
  if (i !== 0) {
    if (n === 0) console.log('1 0');
    else console.log(`${arr[n][0]} ${arr[n][1]}`);
  }
});
