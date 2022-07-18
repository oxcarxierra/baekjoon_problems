# 계단 오르기

import sys
N = int(sys.stdin.readline())
max_score = [0]*(N+1)
stair=[0]
for _ in range(N):
   stair.append(int(sys.stdin.readline()))
max_score[1]=stair[1]
if N>= 2:
   max_score[2]=stair[1]+stair[2]
   for i in range(3,N+1):
      max_score[i] = max(max_score[i-2],max_score[i-3]+stair[i-1])+stair[i]
print(max_score[N])