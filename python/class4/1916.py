# 최소비용 구하기
import heapq
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
  s,e,w = map(int, input().split())
  graph[s].append((e,w))
a,b = map(int, input().split())

distance = [INF]*(n+1)
visited = [False]*(n+1)

def get_smallest_node():
  min_value = INF
  index = 0
  for i in range(1,n+1):
    if not visited[i] and distance[i] < min_value:
      index = i
      min_value = distance[i]
  return index

def dijkstra():
  q = []
  distance[a] = 0
  heapq.heappush(q, (0, a))
  while q:
    dist, node = heapq.heappop(q)
    if distance[node] < dist:
      continue
    for (j,v) in graph[node]:
      cost = distance[node]+ v
      if distance[j] > cost:
        distance[j] = cost
        heapq.heappush(q, (cost, j))
  print(distance[b])

dijkstra()

