# 행렬 곱셈 순서

n = int(input())
size = []
for _ in range(n):
  size.append(list(map(int, input().split())))
dp = [[0]*n for _ in range(n)]

for j in range(n):
  for i in range(n-j):
    if j == 0:
      dp[i][i] = 0
    elif j == 1:
      dp[i][i+1] = size[i][0]*size[i][1]*size[i+1][1]
    else:
      arr = []
      for k in range(0,j):
        arr.append(dp[i][i+k] + dp[i+k+1][i+j] + size[i][0]*size[i+k][1]*size[i+j][1])
      dp[i][i+j] = min(arr)

print(dp[0][n-1])
