import sys

n, m = map(int, sys.stdin.readline().split())
def gcd(n,m):
    p = n
    q = m
    while True:
        if p == q:
            return p
        elif p > q:
            if p % q == 0:
                return q
            else:
                p = p % q
        else:
            if q % p == 0:
                return p
            else:
                q = q % p

print(gcd(n,m))
print(int(m*n/gcd(n,m)))
