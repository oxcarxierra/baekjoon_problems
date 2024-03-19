# 이중 우선순위 큐

import heapq
import sys
T = int(sys.stdin.readline())

def operate(k):
  min_heap, max_heap=[],[]
  visited =[False]*k
  for i in range(k):
    op, num = map(str, sys.stdin.readline().split())
    num = int(num)
    if op == 'I':
      heapq.heappush(min_heap, (num,i))
      heapq.heappush(max_heap, ( -1 * num,i))
      visited[i] = True

    elif op == 'D':
      if num == -1:
        while min_heap and not visited[min_heap[0][1]]:
          heapq.heappop(min_heap)
        if min_heap:
          visited[min_heap[0][1]] = False
          heapq.heappop(min_heap)
      if num == 1:
        while max_heap and not visited[max_heap[0][1]]:
          heapq.heappop(max_heap)
        if max_heap:
          visited[max_heap[0][1]] = False
          heapq.heappop(max_heap)

  while min_heap and not visited[min_heap[0][1]]:
    heapq.heappop(min_heap)
  while max_heap and not visited[max_heap[0][1]]:
    heapq.heappop(max_heap)

  if min_heap and max_heap:
    print(-max_heap[0][0], end=' ')
    print(min_heap[0][0])
  else:
    print("EMPTY")

for _ in range(T):
  k = int(sys.stdin.readline())
  operate(k)
#     print("EMPTY")
# heap 하나로 푸는 경우 -> 시간초과
# def operate(k):
#   heap = []
#   for _ in range(k):
#     op, num = map(str, sys.stdin.readline().split())
#     num = int(num)
#     if op=='I':
#       heapq.heappush(heap, num)
#     elif op=='D' and heap:
#       if num==-1:
#         heapq.heappop(heap)
#       elif num==-1:
#         heap = heapq.nlargest(len(heap), heap)[1:]
#         heapq.heapify(heap)
#   if heap:
#     print(heapq.nlargest(1, heap)[0], end=' ')
#     print(heapq.nsmallest(1, heap)[0])
#   else:
#     print("EMPTY")
