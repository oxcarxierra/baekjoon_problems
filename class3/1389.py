# 케빈 베이컨의 6단계 법칙

import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1,N+1)}
for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  if b not in graph[a]:
    graph[a].append(b)
    graph[b].append(a)

def bacon_number(n):
  q= deque([n])
  visited= [0]*(N+1)
  while q:
    i = deque.pop(q)
    for j in graph[i]:
      if visited[j] == 0:
        deque.appendleft(q,j)
        visited[j] = visited[i] +1
  return sum(visited)

bacon={}
for i in range(1,N+1):
  bacon[i] = bacon_number(i)
print(min(bacon, key=bacon.get))