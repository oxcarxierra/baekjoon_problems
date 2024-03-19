import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt_0, cnt_1 = 0, 0

def count(x,y, size):
  global cnt_0, cnt_1
  color = paper[x][y]
  for i in range(size):
    for j in range(size):
      if paper[x+i][y+j] != color:
        count(x, y, size//2)
        count(x+size//2, y, size//2)
        count(x, y+size//2, size//2)
        count(x+size//2, y+size//2, size//2)
        return
  if color:
    cnt_1 += 1
  else:
    cnt_0 += 1
count(0, 0, N)
print(cnt_0)
print(cnt_1)

