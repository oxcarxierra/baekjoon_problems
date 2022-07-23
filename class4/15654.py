# N과 M(5)
import sys
N, M = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
lst = []
visited = [False]*N


def dfs():
    if len(lst) == M:
        print(*lst)
        return
    for i in range(0, N):
        if not visited[i]:
            visited[i] = True
            lst.append(num[i])
            dfs()
            visited[i] = False
            lst.pop()


dfs()
