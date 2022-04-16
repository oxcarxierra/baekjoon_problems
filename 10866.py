import sys
from collections import deque

N = int(sys.stdin.readline().strip())
arr = deque([])

for _ in range(N):
    word = str(sys.stdin.readline().strip())
    if word.split()[0] == "push_front":
        arr.appendleft(int(word.split()[1]))
    elif word.split()[0] == 'push_back':
        arr.append(int(word.split()[1]))
    elif word == 'pop_front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.popleft())
    elif word == 'pop_back':
        if len(arr) == 0:
            print(-1)
        else: 
            print(arr.pop())
    elif word =='size':
        print(len(arr))
    elif word == 'empty':
        print(1 if len(arr)==0 else 0)
    elif word == 'front':
        if len(arr) == 0:
            print(-1)
        else: 
            print(arr[0])
    elif word == 'back':
        if len(arr) == 0:
            print(-1)
        else: 
            print(arr[-1])