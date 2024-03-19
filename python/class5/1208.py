# 부분수열의 합 2
from itertools import combinations

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt =0
arr1,arr2 = arr[:n//2], arr[n//2:]
sub1, sub2= [], []
for i in range(len(arr1)+1):
  for sub in combinations(arr1, i):
    sub1.append(sum(sub))
for i in range(len(arr2)+1):
  for sub in combinations(arr2, i):
    sub2.append(sum(sub))
sub1.sort()
sub2.sort(reverse=True)

a,b = 0,0
while a < len(sub1) and b < len(sub2):
  if sub1[a] + sub2[b] == s:
    c1 = 1
    c2 = 1
    a += 1
    b += 1
    while a < len(sub1) and sub1[a] == sub1[a-1]:
      c1 += 1
      a += 1
    while b < len(sub2) and sub2[b] == sub2[b-1]:
      c2 += 1
      b += 1
    cnt += c1*c2
  elif sub1[a] + sub2[b] > s:
    b += 1
  else:
    a += 1

print(cnt -1 if s == 0 else cnt)

