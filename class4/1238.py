# 파티
import heapq
INF = int(1e9)
n, m ,x= map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  s, e, w = map(int, input().split())
  graph[s].append([e,w])

def dijkstra(start, end):
  distance = [INF]*(n+1)
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))
  while q:
    [dist, node] = heapq.heappop(q)
    if distance[node] < dist:
      continue
    for [j,v] in graph[node]:
      cost = distance[node] + v
      if distance[j] > cost:
        distance[j] = cost
        heapq.heappush(q,[cost, j])
  return distance[end]

max_time = 0
for i in range(1,n+1):
  max_time = max(max_time, dijkstra(i, x)+ dijkstra(x,i))
print(max_time)