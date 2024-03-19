# 두 배열의 합
import sys
input = sys.stdin.readline
T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

def prefix_sum(arr):
  prefix = []
  for i in range(len(arr)):
    if i == 0:
      prefix.append(arr[i])
    else:
      prefix.append(arr[i-1]+prefix[i-1])
  return prefix

SA , SB = prefix_sum(A), prefix_sum(B)

def partial_sum_B(N):
  cnt = 0
  i, j  = 0,0
  if SB[i] - SB[j] == N:
    cnt += 1
  if SB[i] - SB[j] > N:
    i+= j
    

