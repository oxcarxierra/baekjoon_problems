# A -> B
from collections import deque


a, b= map(int, input().split())

def bfs():
  dp = {}
  dp[a] = 1
  q = deque([a])
  while q:
    x = deque.popleft(q)
    if x == b:
      return dp[b]
    for i in [2*x, 10*x+1]:
      if i <= b:
        dp[i] = dp[x]+1
        deque.append(q, i)
  return -1

print(bfs())