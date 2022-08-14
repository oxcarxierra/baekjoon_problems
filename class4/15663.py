# N과 M (9)

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
n = len(numbers)
dic = {}
lst = []
visited = [0]*n

def dfs():
  if len(lst) == m:
    l = ' '.join(map(str,lst))
    if l not in dic:
      dic[l] = 0
      print(*lst)
    return
  for i in range(n):
    if visited[i]:
      continue
    lst.append(numbers[i])
    visited[i] = True
    dfs()
    visited[i] = False
    lst.pop()

dfs()

