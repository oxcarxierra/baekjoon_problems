# 구간합 구하기 4

import sys
N, M = map(int, sys.stdin.readline().strip().split())
num = list(map(int, sys.stdin.readline().strip().split()))
for i in range(1,N):
    num[i]+=num[i-1]
for _ in range(M):
    i,j = map(int, sys.stdin.readline().strip().split())
    if i == 1:
        print(num[j-1])
    else:
        print(num[j-1]-num[i-2])