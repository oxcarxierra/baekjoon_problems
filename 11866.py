import sys
from collections import deque

N, k = map(int, sys.stdin.readline().split())
res = []
circle = deque(list(range(1, N+1)))
while len(circle)>0:
    circle.rotate(-k+1)
    res.append(circle.popleft())

string_res = [str(int) for int in res]
print(f"<{', '.join(string_res)}>")