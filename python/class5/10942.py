# 팰린드롬?

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

dp = [[-1]*(N) for _ in range(N)]
for i in range(N):
  for j in range(i,N):
    if i == j:
      dp[i][j] = 1
    elif j == i+1:
      dp[i][j] = (1 if arr[i] == arr[i+1] else 0)
    else:
      if arr[i] == arr[j]:
        dp[i][j] = dp[i+1][j-1]
      else:
        dp[i][j] = 0

print(dp)

for _ in range(M):
  a,b= map(int, input().split())
  print(dp[a-1][b-1])
