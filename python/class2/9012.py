import sys

T = int(sys.stdin.readline().strip())
arr = []
for _ in range(T):
    arr.append(str(sys.stdin.readline().strip()))

def is_VPS(str):
    a = 0
    b = 0
    i = 0
    while i < len(str):
        if str[i] == '(':
            a += 1
        elif str[i] == ')':
            b += 1
        if b > a:
            return False
        i+= 1
    if a != b:
        return False
    else:
        return True
    
for i in range(T):
    print('YES' if is_VPS(arr[i]) else 'NO')