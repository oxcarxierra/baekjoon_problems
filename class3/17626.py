# Four Squares

import sys
N = int(sys.stdin.readline())
dp = [0,1]

for i in range(2,N+1):
  j = 1
  min_value = 1e9
  while j*j <= i :
    min_value = min(dp[i-j*j], min_value)
    j += 1
  dp.append(min_value+1)

print(dp[N])