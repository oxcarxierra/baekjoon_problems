# 토마토
import sys
from collections import deque
M, N, H = map(int, sys.stdin.readline().split())
box = []
for _ in range(H):
    layer = []
    for _ in range(N):
        layer.append(list(map(int, sys.stdin.readline().split())))
    box.append(layer)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]


def bfs():
    q = deque()
    cnt = 0
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 1:
                    q.append([x, y, z])
    if not q:
        print(-1)
        return
    while q:
        [x, y, z] = q.popleft()
        for i in range(6):
            if 0 <= x+dx[i] < M and 0 <= y+dy[i] < N and 0 <= z+dz[i] < H and box[z+dz[i]][y+dy[i]][x+dx[i]] == 0:
                q.append([x+dx[i], y+dy[i], z+dz[i]])
                box[z+dz[i]][y+dy[i]][x+dx[i]] = box[z][y][x] + 1
                cnt = box[z][y][x]
    for z in range(H):
        for y in range(N):
            for x in range(M):
                if box[z][y][x] == 0:
                    print(-1)
                    return
    print(cnt)


bfs()
