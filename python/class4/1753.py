# 최단경로
# Dijkstra Algorithm with normal search

INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
graph= [[] for _ in range(V+1)]
for _ in range(E):
  u, v, w= map(int, input().split())
  graph[u].append((v,w))

distance = [INF]*(V+1)
visited = [False]*(V+1)

def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1, V+1):
    if not visited[i] and distance[i] < min_value:
      index = i
      min_value = distance[i]
  return index

def dijkstra():
  visited[K] = True
  distance[K] = 0
  for (i,v) in graph[K]:
    distance[i] = v
  for _ in range(V-1):
    i = get_smallest_node()
    visited[i] = True
    for (j,v) in graph[i]:
      if distance[j] > distance[i] + v:
        distance[j] = distance[i]+ v

dijkstra()

for i in range(1, V+1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])