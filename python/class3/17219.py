# 비밀번호 찾기

import sys
N, M = map(int, sys.stdin.readline().split())
dic = {}
for _ in range(N):
    site, pw = map(str, sys.stdin.readline().strip().split())
    dic[site] = pw
for _ in range(M):
    site = sys.stdin.readline().strip()
    print(dic[site])