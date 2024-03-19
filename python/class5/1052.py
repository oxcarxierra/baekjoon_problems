# 물병

n, k = map(int, input().split())
cnt = 0
while bin(n).count('1') > k:
  b = bin(n)
  idx = len(b)-b.rfind('1')-1
  n += (1 << idx)
  cnt += (1 << idx)
print(cnt)