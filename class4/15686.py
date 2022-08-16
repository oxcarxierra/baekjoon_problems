# 치킨 배달
import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
home = []
store =[]

for x in range(n):
  row = list(map(int,input().split()))
  for y in range(n):
    if row[y] == 2:
      store.append([x,y])
    elif row[y] == 1:
      home.append([x,y])

def nearest(i,j):
  d = 999999
  for [x,y] in selected:
    d = min(d, abs(i-x)+abs(j-y))
  return d

def chicken():
  chicken = 0
  for [x,y] in home:
    chicken += nearest(x,y)
  return chicken

min_chicken = 999999
for selected in combinations(store, m):
  min_chicken = min(min_chicken, chicken())
print(min_chicken)