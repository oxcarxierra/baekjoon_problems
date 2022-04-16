import sys

N = int(sys.stdin.readline().strip())
arr = []
for _ in range(N):
    arr.append(str(sys.stdin.readline().strip()))
arr = list(set(arr))

for i in range(len(arr)):
    for j in range(i,len(arr)):
        if len(arr[i]) > len(arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        elif (len(arr[i]) == len(arr[j])) & (arr[i] > arr[j]):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

for i in range(len(arr)):
    print(arr[i])