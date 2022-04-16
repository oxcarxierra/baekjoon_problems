import sys
n = int(sys.stdin.readline().strip())
m = str(bin(n))[2:]
cnt = 0
for i in range(len(m)):
    if m[i] == '1':
        cnt+=1
print(cnt)