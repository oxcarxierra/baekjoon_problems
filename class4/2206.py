# 벽 부수고 이동하기

from collections import deque
n, m = map(int, input().split())
map = [[int(i) for i in input()] for _ in range(n)]
dp = [[[0,0] for _ in range(m)] for _ in range(n)]

def bfs():
  q = deque()
  deque.append(q, [0,0,0])
  dp[0][0][0] = 1
  dx, dy = [0,0,-1,1], [-1, 1, 0, 0]
  while q:
    [y,x,b] = deque.popleft(q)
    if y==n-1 and x== m-1:
      return dp[n-1][m-1][b]
    for i in range(4):
      if 0 <= y+dy[i] < n and 0 <= x+dx[i] < m and dp[y+dy[i]][x+dx[i]][b] == 0:
        if map[y+dy[i]][x+dx[i]] == 0:
          dp[y+dy[i]][x+dx[i]][b] = dp[y][x][b]+ 1
          deque.append(q,[y+dy[i], x+dx[i],b])
        elif b==0:
          dp[y+dy[i]][x+dx[i]][1] = dp[y][x][0] + 1
          deque.append(q, [y+dy[i],x+dx[i], 1])
  
  return -1
print(bfs())

