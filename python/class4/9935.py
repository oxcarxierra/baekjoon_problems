# 문자열 폭발

import sys
s = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
stack = []
for i in range(len(s)):
  stack.append(s[i])
  if stack[-1] == bomb[-1] and ''.join(stack[-len(bomb):]) == bomb:
    del stack[-len(bomb):]
print('FRULA' if len(stack) == 0 else ''.join(stack))
