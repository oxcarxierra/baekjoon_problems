import sys
lis = []
for i in range(9):
    lis.append(int(sys.stdin.readline()))

max = 0
max_loc = 0
for i in range(9):
    if max < lis[i]:
        max = lis[i]
        max_loc = i+1

print(max)
print(max_loc)
