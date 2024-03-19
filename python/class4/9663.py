# N-Queen

N = int(input())
queen = [0]*(N)
count = 0

def promising(idx):
  for i in range(idx):
    if queen[idx] == queen[i] or abs(queen[idx] - queen[i]) == idx - i:
      return 0
  return 1

def dfs(idx):
  global count
  if idx == N:
    count += 1
    return 
  for i in range(N):
    queen[idx] = i
    if promising(idx):
      dfs(idx+1)

dfs(0)
print(count)
