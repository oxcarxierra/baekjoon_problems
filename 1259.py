import sys

def palindrom(N):
    for i in range(len(N)):
        if N[i] != N[len(N)-1-i]:
            return False
    return True
        
while True:
    N = str(sys.stdin.readline().strip())
    if N == '0':
        break
    else:
        print('yes' if palindrom(N) else 'no')
