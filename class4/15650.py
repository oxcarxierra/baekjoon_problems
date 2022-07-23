# N과 M(2)
import sys
N, M = map(int, sys.stdin.readline().split())

lst = []


def dfs(start):
    # print(*lst)
    if len(lst) == M:
        print(*lst)
        return
    for i in range(start, N+1):
        lst.append(i)
        dfs(i+1)
        lst.pop()


dfs(1)
