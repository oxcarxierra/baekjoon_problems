# 파도반 수열

import sys
t = int(sys.stdin.readline())
P = [0,1,1,1,2,2]
for _ in range(t):
  n = int(sys.stdin.readline())
  if len(P)-1 < n:
      for i in range(len(P), n+1):
          P.append(P[i-1] + P[i-5])
  print(P)
  print(P[n])