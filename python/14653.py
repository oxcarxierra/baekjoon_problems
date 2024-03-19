import sys
from string import ascii_uppercase

N, K, Q = map(int, sys.stdin.readline().split())
arr = []
alphabet_list = list(ascii_uppercase)[1: N]
for _ in range(K):
    arr.append(list(map(str, sys.stdin.readline().split())))

if arr[Q-1][0] == '0':
    print(-1)
else:
    for i in range(Q-1, K-1):
        if arr[i][1] in alphabet_list:
            alphabet_list.remove(arr[i][1])
    print((' ').join(alphabet_list))
