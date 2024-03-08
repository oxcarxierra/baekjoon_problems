# 특정한 최단 경로
import sys
import heapq
INF = int(1e9)
input = sys.stdin.readline
n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
  a,b,c = map(int, input().split())
  graph[a].append([b,c])
  graph[b].append([a,c])
u, v = map(int, input().split())

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

print(min(dijkstra(1,u) + dijkstra(u,v)+ dijkstra(v,n), dijkstra(1,v) + dijkstra(u,v)+ dijkstra(u,n)))