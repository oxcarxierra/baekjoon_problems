import sys

def fac(n):
    res = 1
    if n > 0:
        for i in range(n):
            res *= (i+1)
    return res

n = int(sys.stdin.readline().strip())
for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print(int(fac(b)/(fac(a)*fac(b-a))))