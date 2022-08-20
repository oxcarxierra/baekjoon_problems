# 분해합
n = int(input())
for i in range(n):
    s = i
    for j in str(i):
        s += int(j)
    if s == n:
        print(i)
        exit()
print(0)