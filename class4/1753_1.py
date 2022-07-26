# 최단경로
# Dijkstra Algorithm with binary tree

import heapq

INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph= [[] for _ in range(V+1)]
for _ in range(E):
  u, v, w= map(int, input().split())
  graph[u].append((v,w))

distance = [INF]*(V+1)

def dijkstra():
  q = []
  distance[K] = 0
  heapq.heappush(q, (0, K))
  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    for (j,v) in graph[node]:
      cost = distance[node]+ v
      if distance[j] > cost:
        distance[j] = cost
        heapq.heappush(q, (cost, j))

dijkstra()

for i in range(1, V+1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])