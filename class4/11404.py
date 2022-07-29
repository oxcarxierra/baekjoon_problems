# 플로이드

INF = int(1e9)
n = int(input())
m = int(input())
dist = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
  a, b, c= map(int, input().split())
  dist[a][b] = min(dist[a][b],c)
for i in range(n+1):
  dist[i][i] = 0

for i in range(1,n+1):
  for j in range(1,n+1):
    for k in range(1,n+1):
      dist[j][k] = min(dist[j][k],dist[j][i] + dist[i][k])

for z in range(1,n+1):
    for y in range(1, n+1):
        if dist[z][y] == INF:
            dist[z][y] = 0
    print(*dist[z][1:],sep=" ")

