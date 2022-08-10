# Dance Dance Revolution
import sys
sys.setrecursionlimit(10**6)
ord = list(map(int, input().split()))
length = len(ord) -1 
dp = [[[-1]*5 for _ in range(5)] for _ in range(length)]
move = [[0,2,2,2,2],[0,1,3,4,3],[0,3,1,3,4],[0,4,3,1,3],[0,3,4,3,1]]

def minpower(n,l,r):
  global dp
  if n == length:
    return 0
  if dp[n][l][r] == -1:
    dp[n][l][r] = min(minpower(n+1, ord[n], r) + move[l][ord[n]], minpower(n+1, l, ord[n]) + move[r][ord[n]])
  return dp[n][l][r]

print(minpower(0,0,0))
