# 트리의 지름
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
  a, b, w = map(int, input().split())
  graph[a].append((b,w))
  graph[b].append((a,w))

def dfs(start, wei):
  for node in graph[start]:
    n, w = node
    if dist[n] == -1:
      dist[n] = dist[start] + w
      dfs(n, wei+ w)

dist = [-1]*(n+1)
dist[1] = 0
dfs(1, 0)
start = dist.index(max(dist))
dist = [-1]*(n+1)
dist[start] = 0
dfs(start, 0)

print(max(dist))


