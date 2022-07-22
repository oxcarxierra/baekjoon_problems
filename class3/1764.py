import sys
N, M = map(int, sys.stdin.readline().strip().split())
d_arr = set()
db_arr = []

for _ in range(N):
  d_arr.add(str(sys.stdin.readline().strip()))
for i in range(M):
  name = str(sys.stdin.readline().strip())
  if name in d_arr:
    db_arr.append(name)

print(len(db_arr))
for i in sorted(db_arr):
  print(i)