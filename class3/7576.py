# 토마토

from collections import deque
import sys
M, N = map(int, sys.stdin.readline().strip().split())
box = []
dx = [-1,1,0,0]
dy =[0,0,-1,1]
for _ in range(N):
  box.append(list(map(int, sys.stdin.readline().split())))

def bfs():
  q = deque()
  cnt=0
  for y in range(N):
    for x in range(M):
      if box[y][x] == 1:
        q.append([x,y])
  if not q:
    print(-1)
    return
  while q:
    [x,y] = q.popleft()
    for i in range(4):
      if 0<= x+dx[i] < M and 0 <= y+dy[i] < N and box[y+dy[i]][x+dx[i]] == 0:
        q.append([x+dx[i],y+dy[i]]) 
        box[y+dy[i]][x+dx[i]] = box[y][x] + 1
        cnt= box[y][x]
  for y in range(N):
    for x in range(M):
      if box[y][x] == 0:
        print(-1)
        return
  print(cnt)

bfs()