# 경로 찾기

import sys
from collections import deque
N = int(sys.stdin.readline())
graph = {i:[] for i in range(N)}
for i in range(N):
  row = list(map(int, sys.stdin.readline().split(' ')))
  for j in range(N):
    if row[j] == 1:
      graph[i].append(j)

def connected(i):
  visited = [0]*N
  q = deque()
  deque.append(q, i)
  while q:
    n = deque.pop(q)
    for m in graph[n]:
      if visited[m] == 0:
        visited[m] = 1
        deque.appendleft(q, m)
  print(*visited)

for i in range(N):
  connected(i)