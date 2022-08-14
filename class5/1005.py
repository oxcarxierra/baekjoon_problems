# ACM Craft
import sys
input = sys.stdin.readlines
from collections import deque

T = int(input())
for _ in range(T):
  n, k = map(int, input().split())
  d = [0]
  d.extend(list(map(int, input().split())))
  graph = [[] for _ in range(n+1)]
  in_deg = [0]*(n+1)
  q = deque([])
  t = []
  min_time = [0]*(n+1)
  visited = [False] *(n+1)
  for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)
    in_deg[y] += 1
  w = int(input())

  for i in range(1,n+1):
    if in_deg[i] == 0:
      q.append(i)
      visited[i] = True

  while q:
    node = q.popleft()
    t.append(node)
    for next in graph[node]:
      in_deg[next] -= 1
      if in_deg[next] == 0:
        visited[next] = True
        q.append(next)
  min_time[t[0]] = d[t[0]]
  for x in t:
    for y in graph[x]:
      min_time[y] = max(min_time[y], min_time[x] + d[y])

  print(min_time[w])
