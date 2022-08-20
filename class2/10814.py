import sys

N = int(sys.stdin.readline().strip())
arr= []
for _ in range(N):
    age, name = map(str, sys.stdin.readline().split())
    arr.append([age, name])

arr.sort(key=lambda a:int(a[0]))

for i in range(N):
    print(f"{arr[i][0]} {arr[i][1]}")
