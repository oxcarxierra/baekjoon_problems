# 도시 분할 계획
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for _ in range(m):
  s, e, w = map(int, input().split())
  graph.append([w,s,e])

parent = [i for i in range(n+1)]
rank = [0 for _ in range(n+1)]

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
  max_weight = 0
  graph.sort()
  for w,s,e in graph:
    if find(s) != find(e):
      union(s,e)
      tot_weight += w
      max_weight = max(w, max_weight)
  return tot_weight - max_weight

print(kruskal())