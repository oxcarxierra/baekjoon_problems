# 숨바꼭질 3
# 0-1 bfs

from collections import deque
N, K = map(int, input().split())
map = [1e9]*100001

def bfs():
  map[N] = 0
  q = deque([N])
  while q:
    x = deque.popleft(q)
    if x*2 <=100000 and map[x*2] > map[x]:
      map[x*2] = map[x]
      deque.appendleft(q,x*2)
    for i in [x+1, x-1]:
      if 0 <= i <= 100000 and map[i] > map[x]+1:
         map[i] = map[x] + 1
         deque.append(q,i)

bfs()
print(map[K])