# 패션왕 신해빈

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dic = {}
    answer=1
    for _ in range(n):
        name, cat = map(str, sys.stdin.readline().strip().split())
        if cat in dic.keys():
            dic[cat].append(name)
        else:
            dic[cat] = [name]
    for category in dic.keys():
        answer *= (len(dic[category])+1)
    print(answer-1)