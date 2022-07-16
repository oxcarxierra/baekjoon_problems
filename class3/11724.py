# 연결 요소의 개수
# BFS
from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
cnt = 0
visited = [0]*(N+1)

def bfs(n):
  global cnt
  cnt += 1
  queue = deque([n])
  while queue:
    a = queue.popleft()
    for i in graph[a]:
      if not visited[i]:
        visited[i] = 1
        queue.append(i)

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1,N+1):
  if visited[i] == 0:
    bfs(i)

print(cnt)