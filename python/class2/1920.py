import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
B = list(map(int, sys.stdin.readline().split()))

A.sort()
def binary_search(x):
    start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if x== A[mid]:
            return True
        elif x > A[mid]:
            start = mid + 1
        elif x < A[mid]:
            end = mid - 1
    return False

for i in range(len(B)):
    print('1' if binary_search(B[i]) else '0')

