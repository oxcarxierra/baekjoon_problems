# 트리 순회

N = int(input())
graph = {}
for _ in range(N):
  node, left, right = input().split()
  graph[node]= [left, right] 
preorder, inorder, postorder= [], [], []

def dfs(start):
  preorder.append(start)
  if graph[start][0] != '.':
    dfs(graph[start][0])
  inorder.append(start)
  if graph[start][1] != '.':
    dfs(graph[start][1])
  postorder.append(start)

dfs('A')

print(*preorder, sep='')
print(*inorder, sep='')
print(*postorder, sep='')