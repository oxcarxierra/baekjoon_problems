# 구간 합 구하기 5

N, M = map(int, input().split())
arr = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
s = [list(map(int, input().split())) for i in range(N)]
for i in range(N):
  for j in range(N):
    arr[i + 1][j + 1] = (arr[i][j + 1] + arr[i + 1][j] - arr[i][j]) + s[i][j]
for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  print(arr[x2][y2]-arr[x2][y1-1]-arr[x1-1][y2]+arr[x1-1][y1-1])




