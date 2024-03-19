# 2xn 타일링 2
import sys
n = int(sys.stdin.readline())
P = [1]*(n+1)
for i in range(2, n+1):
  P[i] = P[i-1] + 2* P[i-2]
print(P[n]%10007)