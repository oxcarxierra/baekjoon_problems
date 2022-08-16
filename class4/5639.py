#이진 검색 트리
import sys
sys.setrecursionlimit(10**9)

q = []
while True:
  try:
    n = int(sys.stdin.readline())
    q.append(n)
  except:
    break

def post(start, end):
  if end < start:
    return
  if end == start:
    print(q[start])
    return
  root = q[start]
  for i in range(start+1, end+1):
    if q[i] > root:
      post(start+1, i-1)
      post(i,end)
      print(root)
      return
  post(start+1, end)
  print(root)

post(0, len(q)-1)

