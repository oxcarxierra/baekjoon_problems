const d = (n) => {
  let res = n;
  String(n)
    .split('')
    .forEach((i) => (res += Number(i)));
  return res;
};

const arr = [];
for (let i = 1; i <= 10000; i++) {
  arr.push(d(i));
}
const arr2 = [];
for (let i = 1; i <= 10000; i++) {
  if (!arr.includes(i)) arr2.push(i);
}

arr2.forEach((i) => console.log(i));
