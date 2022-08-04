# 부분합
n, s = map(int, input().split())
num = list(map(int, input().split()))

def sps():
  pl, pr = 0, 0
  p_sum, min_len = num[0], n+1
  while True:
    if p_sum < s:
      pr += 1
      if pr == n: 
        print(0 if min_len == n+1 else min_len)
        return
      p_sum += num[pr]
    else:
      if min_len > pr-pl+1:
        min_len = pr - pl + 1
      p_sum -= num[pl]
      pl += 1

sps()

