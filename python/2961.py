# 도영이가 만든 맛있는 음식

from itertools import combinations
n = int(input())
ing= []
min_abs = int(1e9)
for _ in range(n):
  ing.append(list(map(int, input().split())))
for i in range(1, n+1):
  for com in combinations(ing, i):
    s, b = 1, 0
    for j in range(i):
      s *= com[j][0]
      b += com[j][1]
    min_abs = min(min_abs, abs(s-b))

print(min_abs)