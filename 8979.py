import sys

N, k = map(int, sys.stdin.readline().split())
arr = []
target_arr = []
cnt = 0
for _ in range(N):
    new_arr = list(map(int, sys.stdin.readline().split()))
    if new_arr[0] == k:
        target_arr = new_arr
    arr.append(new_arr)

for i in range(N):
    if arr[i][1] > target_arr[1]:
        cnt += 1
    elif (arr[i][1] == target_arr[1]) & (arr[i][2] > target_arr[2]):
        cnt += 1
    elif (arr[i][1] == target_arr[1]) & (arr[i][2] == target_arr[2]) & (arr[i][3] > target_arr[3]):
        cnt += 1

print(cnt+1)

