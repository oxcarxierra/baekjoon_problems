# N과 M (8)

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
lst = []

def dfs(start):
  if len(lst) == m:
    print(*lst)
    return
  for i in range(start, n):
    lst.append(numbers[i])
    dfs(i)
    lst.pop()

dfs(0)