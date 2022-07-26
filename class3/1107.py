# 리모컨

import sys
N = sys.stdin.readline().strip()
M = int(sys.stdin.readline())
for _ in range(M):
  broken = list(map(int, sys.stdin.readline().split()))

direct = abs(100-int(N))
lower, upper = 0, 0
if broken:
  for i in range(len(N)):
    if i in broken:
      for x in range(10):
        
