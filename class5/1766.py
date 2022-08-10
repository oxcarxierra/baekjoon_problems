# 문제집
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indeg = [0]*(n+1)
for _ in range(m):
  a, b= map(int, input().split())
  graph[a].append(b)
  indeg[b] += 1

visited = [False]*(n+1)
t , q =[], []

for i in range(1, n+1):
  if indeg[i] == 0:
    heapq.heappush(q,i)
    visited[i] = True

while q:
  node = heapq.heappop(q)
  t.append(node)
  for next in graph[node]:
    indeg[next] -= 1
    if indeg[next] == 0:
      visited[next] = True
      heapq.heappush(q, next)

print(*t)


