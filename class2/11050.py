import sys 

N, K = map(int, sys.stdin.readline().split())

def fac(n):
    res= 1
    for i in range(1,n+1):
        res *= i
    return res

print(int(fac(N)/fac(K)/fac(N-K)))