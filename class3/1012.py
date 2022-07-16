from collections import deque
import sys
T = int(sys.stdin.readline())
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(x,y,visited):
  queue = deque()
  queue.append([x,y])
  visited[x][y] = 0
  while queue:
    [a, b]= queue.pop()
    for i in range(4):
      nx=a+dx[i]
      ny=b+dy[i]
      if 0<=nx<M and 0 <= ny < N and visited[nx][ny] == 1:
        visited[nx][ny] = 0
        queue.appendleft([nx,ny])
  return

for _ in range(T):
  M, N, K = map(int, sys.stdin.readline().split())
  cnt=0
  visited = [[0]*N for _ in range(M)]
  for _ in range(K):
    X, Y = map(int, sys.stdin.readline().split())
    visited[X][Y]=1
  for x in range(M):
    for y in range(N):
      if visited[x][y] == 1:
        cnt += 1
        bfs(x,y,visited)
  print(cnt)
