# 소수의 연속합

N = int(input())

def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우 
            for j in range(i+i, n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    # 소수 목록 산출
    return [i for i in range(2, n+1) if sieve[i] == True]

def count(n):
  if n ==1:
    return 0
  prime = prime_list(n)
  pl, pr, ps, cnt = 0, 0, prime[0], 0
  while True:
    if ps == n:
      cnt += 1
    if ps <= n:
      if pr == len(prime)-1:
        return cnt
      else:
        pr += 1
        ps += prime[pr]
    else:
      ps -= prime[pl]
      pl += 1

print(count(N))

