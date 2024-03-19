import sys

a, b = map(int, sys.stdin.readline().split())
i = 0
arr = []
while True:
    if len(arr)>b:
        break
    for _ in range(i):
        arr.append(i)
    i += 1
res = 0
for j in range(a,b+1):
    res += arr[j-1]
print(res)

