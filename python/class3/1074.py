# Z
import sys
N, r, c= map(int, sys.stdin.readline().split())

def get_order(N, x, y):
  if N == 1:
    return [0,1,2,3][x*2+y]
  else:
    n_x, n_y = x%(2**(N-1)), y%(2**(N-1))
    return get_order(N-1, n_x, n_y) + (x//(2**(N-1)) * 2 + y//(2**(N-1)))*4**(N-1)

print(get_order(N, r, c))
