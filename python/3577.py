res = 1
lis = [0,0,0,0,0,0,0,0,0,0]
for _ in range(3):
    res *= int(input())
res = str(res)
for i in range(len(res)):
    lis[int(res[i])]+= 1
for i in range(len(lis)):
    print(lis[i])
