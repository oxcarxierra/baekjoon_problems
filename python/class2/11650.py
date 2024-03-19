import sys

N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(tuple(map(int, sys.stdin.readline().split())))

arr.sort(key= lambda x : (x[0], x[1]))
for i in range(N):
    print(arr[i][0], arr[i][1])