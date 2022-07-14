import heapq
import sys
N = int(sys.stdin.readline())
heap = []

for _ in range(N):
  input = int(sys.stdin.readline())
  if input == 0:
    if heap:
      print(heapq.heappop(heap))
    else:
      print(0)
  else:
    heapq.heappush(heap, input)

# 최소 힙 직접 구현
# heap=[0]
# def add(n):
#   heap.append(n)
#   idx = len(heap)-1
#   while idx > 1:
#     if heap[idx] < heap[idx//2]:
#       heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
#     idx = idx // 2
#   return
# def delete():
#   if len(heap) == 1:
#     print(0)
#   else:
#     print(heap[1])
#     heap[1] = heap[-1]
#     heap.pop()
#     idx = 1
#     while idx <= (len(heap)-1)//2:
#       if heap[idx] > heap[idx*2]:
#         heap[idx], heap[idx*2] = heap[idx*2],heap[idx]
#         idx = idx*2
#       elif idx*2+1 <= len(heap)-1 and heap[idx] < heap[idx*2+1]:
#         heap[idx], heap[idx*2+1] = heap[idx*2+1],heap[idx]
#         idx = idx*2 + 1
#       else:
#         break

# for _ in range(N):
#   input = int(sys.stdin.readline())
#   if input == 0:
#     delete()
#   else:
#     add(input)