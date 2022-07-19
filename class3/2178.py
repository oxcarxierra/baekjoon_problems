# 미로 탐색
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
map_arr = []
for _ in range(N):
  row = sys.stdin.readline().strip()
  map_arr.append([row[i] for i in range(M)])

route = deque([[0,0]])
map_arr[0][0] = 0
while route:
  spot = deque.pop(route)
  x = spot[0]
  y = spot[1]
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  for i in range(4):
    if 0 <= x+dx[i] < M and 0 <= y+dy[i] < N and map_arr[y+dy[i]][x+dx[i]] == '1':
      map_arr[y+dy[i]][x+dx[i]] = map_arr[y][x] + 1
      route.appendleft([x+dx[i], y+dy[i]])
print(map_arr[N-1][M-1]+1)
