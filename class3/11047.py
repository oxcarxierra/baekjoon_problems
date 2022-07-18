# 동전 0
import sys
N, K = map(int, sys.stdin.readline().split())
coins = []
cnt = 0
for _ in range(N):
  coin = int(sys.stdin.readline())
  if coin <= K:
    coins.append(coin)
i = len(coins)-1
while K > 0:
  if K >= coins[i]:
    cnt += K // coins[i]
    K = K % coins[i]
  else:
    i -= 1
print(cnt)
