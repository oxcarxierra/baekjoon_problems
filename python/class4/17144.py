# 미세먼지 안녕!
import copy

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

def purifier():
  for x in range(r):
    if room[x][0] == -1:
      return x


def diffusion():
  global room
  d = [[0]*c for _ in range(r)]
  dx, dy  = [1,-1,0,0],[0,0,1,-1]
  for x in range(r):
    for y in range(c):
      if room[x][y] > 0:
        for i in range(4):
          nx, ny= x + dx[i], y+dy[i]
          if 0 <= nx <= r-1 and 0 <= ny < c and room[nx][ny] != -1:
            d[nx][ny] += room[x][y] // 5
            d[x][y] -= room[x][y] // 5
  for x in range(r):
    for y in range(c):
      room[x][y] += d[x][y]
  return

def cycle():
  global room
  after= copy.deepcopy(room)
  for i in range(c-1):
    after[0][i] = room[0][i+1]
    after[-1][i] = room[-1][i+1]
  for i in range(1,p):
    after[i][0] = room[i-1][0]
  for i in range(p):
    after[i][-1] = room[i+1][-1]
  for i in range(1,c):
    after[p][i] = room[p][i-1]
    after[p+1][i] = room[p+1][i-1]
  for i in range(p+2,r-1):
    after[i][0] = room[i+1][0]
  for i in range(p+2, r):
    after[i][-1] = room[i-1][-1]
  after[p][1], after[p+1][1] = 0, 0
  room = after
  return

# def printroom():
#   for i in range(r):
#     print(*room[i])
#   print('-----------------')

p = purifier() 
for _ in range(t):
  diffusion()    
  # printroom()
  cycle()
  # printroom()

pm = 0
for i in range(r):
  for j in range(c):
    pm += room[i][j] if room[i][j] > 0 else 0
print(pm)