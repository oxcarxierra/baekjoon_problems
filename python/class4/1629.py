# 곱셈

import sys

A, B, C = map(int, sys.stdin.readline().split())
ans = 1
A %= C
B = bin(B)[2:]

for i in B:
  if i == '1':
    ans = (ans ** 2) * A % C
  else:
    ans = ans **2 % C
print(ans)
