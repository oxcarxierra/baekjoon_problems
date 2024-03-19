# 1의 개수 세기

a, b = map(int, input().split())
psum = [0 for _ in range(60)]
for i in range(1,60):
  psum[i] = 2**(i-1) + psum[i-1]*2 

def count(num):
  cnt = 0
  bi = bin(num)[2:]
  length = len(bi)
  for i in range(length):
    if bi[i] == '1':
      pow = length - 1- i
      cnt += psum[pow]
      cnt += (num-2**pow + 1)
      num = num - 2**pow
  return cnt

print(count(b) - count(a-1))