# 조합
import sys
n, m = map(int, sys.stdin.readline().split())

sol = 1
for i in range(1,min(m, n-m)+1):
  sol = sol * (n-i+1) // i

print(sol)