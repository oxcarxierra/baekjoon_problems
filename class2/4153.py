import sys

while True:
    A, B, C = map(int, sys.stdin.readline().split())
    if A == 0:
        break
    elif 2*(max(A,B,C)**2) == A**2 + B**2 + C**2:
        print('right')
    else:
        print('wrong')