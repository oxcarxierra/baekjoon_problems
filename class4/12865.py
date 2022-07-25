# 평범한 배낭

N, K = map(int, input().split())
items =[list(map(int, input().split())) for _  in range(N)]
dp = [[0]*(K+1) for _ in range(N)]
for i in range(N):
  for j in range(K+1):
    if items[i][0] > j:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]]+ items[i][1])

print(dp[N-1][K])
