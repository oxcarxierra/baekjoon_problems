import sys
N, M = map(int, sys.stdin.readline().strip().split())
dogam = {}
reverse = {}
for i in range(1,N+1):
  name = str(sys.stdin.readline().strip())
  dogam[str(i)] =name
  reverse[name] = str(i)
for i in range(M):
  input = str(sys.stdin.readline().strip())
  if input.isdigit():
    print(dogam[input])
  else:
    print(reverse[input])
