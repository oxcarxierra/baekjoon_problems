import sys
N = int(sys.stdin.readline().strip())
list = list(map(int, sys.stdin.readline().strip().split()))
list.sort()
total_time= 0
for i in range(N):
  total_time += (N-i) * list[i]
print(total_time)