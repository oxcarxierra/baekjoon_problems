# 트리의 지름
v = int(input())
graph = [[] for _ in range(v+1)]
for _ in range(v):
  row = list(map(int, input().split()))
  for i in range(1,len(row),2):
    if row[i] != -1:
      graph[row[0]].append([row[i], row[i+1]])

def dfs(start, wei):
  for x in graph[start]:
    if dist[x[0]] == -1:
      dist[x[0]] = wei + x[1]
      dfs(x[0], wei+x[1])


dist = [-1]*(v+1)
dist[1] = 0
dfs(1, 0)
end = dist.index(max(dist))
dist = [-1]*(v+1)
dist[end] = 0
dfs(end, 0)
print(max(dist))