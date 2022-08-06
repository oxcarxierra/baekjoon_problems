# 알파벳
import sys

input= sys.stdin.readline
r, c = map(int, input().split())
board = []
for _ in range(r):
  row = input()
  board.append([i for i in row])
dx = [1,-1,0,0]
dy = [0,0,1,-1]
path = set()

max_len = 0
def findpath(i,j):
  global max_len
  path.add(board[i][j])
  if len(path) > max_len:
    max_len = len(path)
  for k in range(4):
    ni, nj = i+dx[k], j+dy[k]
    if 0 <= ni <= r-1 and 0 <= nj <= c-1 and board[ni][nj] not in path:
      findpath(ni, nj)
  path.remove(board[i][j])

findpath(0,0)
print(max_len)
