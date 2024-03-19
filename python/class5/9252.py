# LCS 2

a = input()
b = input()
la ,lb = len(a), len(b)
dp = [[0]*(lb+1) for _ in range(la+1)]

for i in range(1, la+1):
  for j in range(1, lb+1):
    if a[i-1] == b[j-1]:
      dp[i][j] = dp[i-1][j-1]+1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])

lcs = []

x,y = la, lb
while x!=0 and y!= 0:
  if dp[x][y] == dp[x-1][y]:
    x -= 1
  elif dp[x][y] == dp[x][y-1]:
    y -= 1
  else:
    lcs.append(a[x-1])
    x-=1
    y -= 1

print(dp[la][lb])
print(*reversed(lcs), sep='')
