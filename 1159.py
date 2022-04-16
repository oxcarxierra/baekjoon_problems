import sys

n = int(sys.stdin.readline())
dic = {}
res=[]
for i in range(n):
    name = str(sys.stdin.readline())[0]
    if name in dic:
        dic[name] += 1
    else:
        dic[name] = 1
for key, value in dic.items():
    if value >= 5:
       res.append(key)
if len(res):
    res.sort()
    print(''.join(res))
else:
    print('PREDAJA')

