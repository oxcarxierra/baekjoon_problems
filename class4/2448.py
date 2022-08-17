# 별 찍기 11

N = int(input())

def star(n):
  if n== 3:
    return[[' ',' ','*',' ',' '],[' ','*',' ','*',' '],['*','*','*','*','*']]
  else:
    m = n//2
    small = star(m)
    tri = [[' ']*(2*n-1) for _ in range(n)]
    for i in range(0,m):
      for j in range(0, 2*m-1):
        tri[i][j+m] = tri[i+m][j] = tri[i+m][j+2*m] = small[i][j]
    return tri

for row in star(N):
  print(''.join(row))