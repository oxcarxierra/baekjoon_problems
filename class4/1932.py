# 정수 삼각형

n = int(input())
tri = []
for i in range(0,n):
  if i == 0:
    tri.append([int(input())])
  else:
    row = list(map(int, input().split()))
    row[0] += tri[i-1][0]
    row[i] += tri[i-1][i-1]
    for j in range(1,i):
      row[j] += max(tri[i-1][j-1], tri[i-1][j])
    tri.append(row)
print(max(tri[n-1]))