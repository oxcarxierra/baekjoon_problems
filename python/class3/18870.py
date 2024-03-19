# 좌표 압축
import sys
N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

sort_X = sorted(list(set(X)))
dic_X = {sort_X[i]: i for i in range(len(sort_X))}

for i in X:
  print(dic_X[i], end=' ')