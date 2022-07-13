import sys
N = int(sys.stdin.readline())
S = set()

for _ in range(N):
  input = sys.stdin.readline().strip().split()
  key = input[0]
  if len(input) == 2:
    value = int(input[1])
    if key=='add':
      S.add(value)
    elif key=='remove':
      S.discard(value)
    elif key=='check':
      print(1 if value in S else 0)
    else:
      if value in S:
        S.discard(value)
      else: 
        S.add(value)
  else:
    if key=='all':
      S = set([i for i in range(1,21)])
    else:
      S = set()