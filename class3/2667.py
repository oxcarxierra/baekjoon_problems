# 단지번호붙이기

import sys
from collections import deque
N = int(sys.stdin.readline())
map_arr = []
building = []
for _ in range(N):
    row = sys.stdin.readline().strip()
    map_arr.append([row[i] for i in range(N)])

def bfs(b,a):
    global map_arr,N
    cnt = 1
    map_arr[b][a] = 1
    q = deque()
    deque.append(q,[b,a])
    while q:
        spot = deque.pop(q)
        y, x = spot[0],spot[1]
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        for i in range(4):
            if 0 <= x+dx[i] < N and 0 <= y+dy[i] < N and map_arr[y+dy[i]][x+dx[i]] == '1':
                map_arr[y+dy[i]][x+dx[i]] = map_arr[y][x]
                deque.appendleft(q, [y+dy[i], x+dx[i]])
                cnt += 1
    return cnt

for i in range(N):
    for j in range(N):
        if map_arr[i][j]=='1':
            building.append(bfs(i,j))
print(len(building))
for x in sorted(building):
    print(x)