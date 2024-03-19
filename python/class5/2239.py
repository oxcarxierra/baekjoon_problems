# 스도쿠

s = [[int(i) for i in input()] for _ in range(9)]
r, c, sq = [[False]*10 for _ in range(9)],[[False]*10 for _ in range(9)],[[False]*10 for _ in range(9)]
for i in range(9):
  for j in range(9):
    x = s[i][j]
    r[i][x] = c[j][x] = sq[(i//3)*3+j//3][x] = True

def solve(cnt):
  global r, c, sq
  if cnt == 81:
    for i in s:
      print(*i, sep='')
    exit()
  x,y = cnt // 9, cnt%9
  if s[x][y] == 0:
    for i in range(1,10):
      if not r[x][i] and not c[y][i] and not sq[(x//3)*3+y//3][i]:
        s[x][y] = i
        r[x][i] = c[y][i] = sq[(x//3)*3+y//3][i] = True
        solve(cnt+1)
        s[x][y] = 0
        r[x][i] = c[y][i] = sq[(x//3)*3+y//3][i] = False
  else:
    solve(cnt+1)

solve(0)


  
