# RGB 거리 2

n = int(input())
INF = int(1e9)
rgb = []
ans = INF
for _ in range(n):
  rgb.append(list(map(int, input().split())))
for c in range(3):
  dp = [[INF,INF,INF]]
  dp[0][c] = rgb[0][c]
  for i in range(1,n):
    r = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
    g = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
    b = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])
    dp.append([r,g,b])
  for j in range(3):
    if c != j:
      ans = min(ans, dp[-1][j])
print(ans)
