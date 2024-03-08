# 테트로미노

import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
max_tetro =0

def bfs(i,j):
  max_sum = 0
  tetro= [[i,j]]
  dx, dy = [-1,1,0,0],[0,0,1,-1]
  for a in range(4):
    i2, j2= i+dx[a], j+dy[a]
    if 0 <= i2 < n and 0 <= j2 < m:
      tetro.append([i2, j2])
      for b in range(4):
        i3, j3= i2+dx[b], j2+dy[b]
        if 0 <= i3 < n and 0 <= j3 < m and [i3,j3] not in tetro:
          tetro.append([i3, j3])
          for c in range(4):
            i4, j4= i3+dx[b], j3+dy[b]
            if 0 <= i4 < n and 0 <= j4 < m and [i4,j4] not in tetro:
              tetro.append([i4, j4])
              max_sum = max(max_sum, paper[i][j]+paper[i2][j2]+paper[i3][j3]+paper[i4][j4])
  return max_sum

for i in range(n):
  for j in range(m):
    max_tetro = max(max_tetro, bfs(i,j))

print(max_tetro)

