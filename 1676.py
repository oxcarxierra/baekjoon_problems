import sys
n = int(sys.stdin.readline())

def get_power(n,k):
  cnt = 0
  while n%k==0:
    n = n/k
    cnt += 1
  return cnt

sum=0
for i in range(1,n+1):
  sum += get_power(i,5)
print(sum)
