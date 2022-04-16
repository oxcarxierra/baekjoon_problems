import sys

N = int(sys.stdin.readline().strip())
arr = []

for _ in range(N):
    word = str(sys.stdin.readline().strip())
    if word.split()[0] == 'push':
        arr.append(word.split()[1])
    elif word == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())
    elif word == 'size':
        print(len(arr))
    elif word == 'empty':
        print(1 if len(arr)== 0 else 0)
    elif word == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])