# 웜홀

TC = int(input())
INF = int(1e9)

def bellman_ford(start):
  dist = [INF]*(n+1)
  dist[start] = 0
  for i in range(n+1):
    for [s,e,t] in graph:
      if  dist[e] > dist[s] + t:
        dist[e] = dist[s] + t
        if i == n:
          return 'YES'
  return 'NO'

for _ in range(TC):
  n, m, w = map(int, input().split())
  graph = []
  for _ in range(m):
    s, e, t = map(int, input().split())
    graph.append([s,e,t])
    graph.append([e,s,t])
  for _ in range(w):
    s, e, t = map(int, input().split())
    graph.append([s,e,-t])
  print(bellman_ford(1))

