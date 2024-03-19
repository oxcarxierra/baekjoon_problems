# 최소 스패닝 트리
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
graph = []
for _ in range(E):
  s,e,w = map(int, input().split())
  graph.append([w,s,e])
parent = [i for i in range(V+1)]
rank = [0 for _ in range(V+1)]

def find(a):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
  a, b = find(a), find(b)
  if a==b:
    return -1
  if rank[a] > rank[b]:
    a, b = b, a
  parent[a] = b
  if rank[a] == rank[b]:
    rank[b] += 1

def kruskal():
  tot_weight = 0
  graph.sort()
  for w,s,e in graph:
    if find(s) != find(e):
      union(s,e)
      tot_weight += w
  return tot_weight

print(kruskal())
