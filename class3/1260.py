# DFS와 BFS

import sys
from collections import deque
N, M, V = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1,N+1)}
for _ in range(M):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
for i in range(1,N+1):
  graph[i].sort()

dfs_visited = [0]*(N+1)
dfs_order = []
def dfs(node):
  global dfs_visited, dfs_order
  dfs_visited[node]=1
  dfs_order.append(node)
  for i in graph[node]:
    if dfs_visited[i] == 0:
      dfs(i)

def bfs():
  visited = [0]*(N+1)
  q = deque([V])
  order = []
  visited[V]=1
  while q:
    i = deque.pop(q)
    order.append(i)
    for j in graph[i]:
      if visited[j]==0:
        deque.appendleft(q,j)
        visited[j] = 1
  print(*order)

dfs(V)
print(*dfs_order)
bfs()