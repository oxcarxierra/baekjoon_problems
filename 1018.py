import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for _ in range(N):
    arr.append(str(sys.stdin.readline().strip()))

def check_minimum(i,j):
    cnt=0
    for x in range(i, i+8):
        for y in range(j, j+8):
            if ((x+y) % 2 == 0) & (arr[x][y] == 'B'):
                cnt += 1
            if ((x+y) % 2 == 1) & (arr[x][y] == 'W'):
                cnt += 1
    return (min(cnt, 8*8-cnt))

res = check_minimum(0,0)

for i in range(0,N-7):
    for j in range(0, M-7):
        temp = check_minimum(i,j)
        if res > temp:
            res = temp

print(res)