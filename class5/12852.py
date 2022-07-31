# 1로 만들기 2

from collections import deque

N = int(input())
dp = [[]for _ in range(N+1)]
q = deque([1])
dp[1].append(1)
def bfs():
  while q:
    x = deque.popleft(q)
    for y in [x+1, x*2, x*3]:
      if y <= N and len(dp[y]) == 0:
        dp[y].extend(dp[x])
        dp[y].append(y)
        deque.append(q, y)

bfs()
print(len(dp[N])-1)
print(*reversed(dp[N]))