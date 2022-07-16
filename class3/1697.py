# 숨바꼭질
from collections import deque
import sys
N, K = map(int, sys.stdin.readline().split())
dist = [0]*100001

def bfs():
  queue = deque()
  queue.append(N)
  while queue:
    x = queue.popleft()
    for i in [x+1, x-1, x*2]:
      if i == K:
        print(dist[x]+1)
        return
      if 0 <= i <= 100000 and dist[i] == 0:
        dist[i] = dist[x] + 1
        queue.append(i)

if N == K:
  print(0)
else:
  bfs()