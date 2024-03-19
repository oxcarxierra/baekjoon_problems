# 음악 프로그램
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
deg = [0]*(n+1)
for _ in range(m):
  row = list(map(int, input().split()))
  for i in range(1,len(row)-1):
    a,b = row[i], row[i+1] 
    graph[a].append(b)
    deg[b] +=1

visited = [False]*(n+1)
t = []
q = deque([])

for i in range(1,n+1):
  if deg[i] == 0:
    deque.append(q,i)
    visited[i] = True

while q:
  node = deque.popleft(q)
  t.append(node)
  for next in graph[node]:
    if not visited[next]:
      deg[next] -= 1
      if deg[next] == 0:
        visited[next] = True
        deque.append(q, next)
    
if len(t) == n:
  print(*t, sep='\n')
else:
  print(0)