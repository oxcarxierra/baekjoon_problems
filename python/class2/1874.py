# 스택 수열
import sys
input = sys.stdin.readline
n = int(input())
p = 1
stack = []
ans = []
temp = True
for _ in range(n):
  x = int(input())
  while p < x:
    stack.append(p)
    ans.append('+')
    p += 1
  if stack[-1] == x:
    stack.pop()
    ans.append('-') 
  else:
    temp = False
    break
if temp:
  print(*ans, sep='\n')
else:
  print("NO")