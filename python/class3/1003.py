import sys

fibonacci = [0,1]
def get_fibonacci(n):
  while len(fibonacci) <= n:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

N = int(sys.stdin.readline().strip())
for _ in range(N):
  n = int(sys.stdin.readline().strip())
  if n==0:
    print('1 0')
  else:
    get_fibonacci(n)
    print(str(fibonacci[n-1])+' '+str(fibonacci[n]))
