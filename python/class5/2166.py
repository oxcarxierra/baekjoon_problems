# 다각형의 면적

n = int(input())
poly= []
s = 0
for _ in range(n):
  x,y = map(int, input().split())
  poly.append([x,y])
poly.append(poly[0])
for i in range(n):
  s += poly[i][0]*poly[i+1][1] - poly[i][1]*poly[i+1][0]
print(abs(s)/2)
