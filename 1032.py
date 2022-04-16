import sys
n = int(sys.stdin.readline())
words=[]
res = ''
for _ in range(n):
    words.append(str(sys.stdin.readline().strip()))

for i in range(len(words[0])):
    res += words[0][i]
    for j in range(n):
        if words[0][i] != words[j][i]:
            res = res[0:-1]
            res+= '?'
            break

print(res)