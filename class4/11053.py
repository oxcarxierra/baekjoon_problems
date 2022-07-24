# 가장 긴  증가하는 부분 수열

# Longest Increasing Subsequence
import sys
N = int(sys.stdin.readline())
A = [0]
A.extend(list(map(int, sys.stdin.readline().split())))
D = [0]*(N+1)

for i in range(1, N+1):
  max_D = 0
  for j in range(0, i):
    if A[j] < A[i]:
      max_D = max(max_D, D[j])
  D[i] = max_D + 1

print(max(D))
