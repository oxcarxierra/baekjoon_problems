# 연구소
import copy
from itertools import combinations
from collections import deque

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
empty = []
wall = []
vi = []
max_safe = 0
for i in range(n):
  for j in range(m):
    if lab[i][j] == 0:
      empty.append([i,j])
    elif lab[i][j] == 1:
      wall.append([i,j])
    else:
      vi.append([i,j])

def bfs(morewall):
  l = copy.deepcopy(lab)
  for [i,j] in morewall:
    l[i][j] = 1
  q = deque([])
  safe = 0
  for v in vi:
    deque.append(q, v)
  dx, dy = [-1,1,0,0],[0 ,0,-1,1]
  while q:
    [x,y] = deque.popleft(q)
    for i in range(4):
      nx, ny = x+dx[i], y+dy[i]
      if 0 <= nx <= n-1 and 0 <= ny <= m-1 and l[nx][ny] == 0:
        deque.append(q, [nx, ny])
        l[nx][ny] = 2
  for i in range(n):
    # print(*l[i])
    for j in range(m):
      if l[i][j] == 0:
        safe += 1
  # print('----------')
  return safe

for morewall in combinations(empty, 3):
  morewall = list(morewall)
  max_safe = max(bfs(morewall), max_safe)

print(max_safe)
