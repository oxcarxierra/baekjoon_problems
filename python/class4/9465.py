# 스티커

T = int(input())
for _ in range(T):
  n = int(input())
  sticker = [[0,0]for _ in range(n+1)]
  for j in range(2):
    row = list(map(int, input().split()))
    for i in range(1,n+1):
      sticker[i][j] = row[i-1]
  
  for i in range(2, n+1):
    sticker[i][0] += max(sticker[i-1][1],sticker[i-2][0], sticker[i-2][1])
    sticker[i][1] += max(sticker[i-1][0],sticker[i-2][0], sticker[i-2][1])
  if n == 1:
    print(max(sticker[n][1],sticker[n][0]))
  else:
    print(max(sticker[n][1],sticker[n][0],sticker[n-1][0], sticker[n-1][1]))
