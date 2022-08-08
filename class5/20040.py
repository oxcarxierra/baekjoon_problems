# 사이클 게임
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n,m = map(int, input().split())
parent = [i for i in range(n)]
rank = [0 for i in range(n)]

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

def cycle():
  for x in range(m):
    a,b= map(int, input().split())
    if union(a,b) == -1:
      print(x+1)
      return
  print(0)

cycle()