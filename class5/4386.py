# 별자리 만들기

n = int(input())
star = []
for _ in range(n):
  x,y = map(float, input().split())
  star.append([x,y])
graph = []
for i in range(n):
  for j in range(i+1, n):
    dist = float(((star[i][0] - star[j][0])**2 + (star[i][1] - star[j][1])**2)**0.5)
    graph.append([dist, i,j])

parent = [i for i in range(n)]
rank = [0 for _ in range(n)]

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