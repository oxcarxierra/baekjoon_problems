# 종이의 개수
import sys
N = int(sys.stdin.readline())
paper= []
cnt = [0,0,0]
for _ in range(N):
  paper.append(list(map(int, sys.stdin.readline().split())))

def check(x,y,n):
  for dx in range(n):
    for dy in range(n):
      if not paper[x+dx][y+dy] == paper[x][y]:
        for i in range(3):
          for j in range(3):
            check(x+(n//3)*i, y+(n//3)*j, n//3)
        return
  cnt[paper[x][y]+1] += 1

check(0,0,N)
print(cnt[0])
print(cnt[1])
print(cnt[2])
