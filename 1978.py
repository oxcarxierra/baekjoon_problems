import sys

def is_prime(N):
    if N < 2:
        return False
    i = 2
    while True:
        if i * i > N:
            return True
        elif N % i == 0:
            return False
        else:
            i+= 1

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
res = 0
for i in range(len(arr)):
    if is_prime(arr[i]):
        res += 1
print(res)
