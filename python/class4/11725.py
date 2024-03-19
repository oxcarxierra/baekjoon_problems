# 트리의 부모 찾기
from collections import deque

N = int(input())
graph = {i:[] for i in range(1,N+1)}

while True:
  try:
    a, b= map(int, input().split())
    graph[b].append(a)
    graph[a].append(b)
  except:
    break

parent = [0]*(N+1)
q = deque([1])
parent[1] = 1
while q:
  i = deque.popleft(q)
  for j in graph[i]:
    if parent[j] == 0:
      parent[j] = i
      deque.append(q, j)

for i in range(2,N+1):
  print(parent[i])