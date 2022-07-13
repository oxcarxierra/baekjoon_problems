import sys
N = int(sys.stdin.readline())
arr = [0]*(N+1)
for i in range(2,N+1):
  arr[i] = arr[i-1] +1
  if i%2 == 0:
    arr[i] = min(arr[i], arr[i//2]+1)
  if i%3 == 0:
    arr[i] = min(arr[i], arr[i//3]+1)
print(arr[N])

# def get_min(n):
#   S = {1}
#   cnt=0
#   if n == 1:
#     print(0)
#   else:
#     while True:
#       cnt+=1
#       next_set = set()
#       for i in S:
#         if n in {i*2, i*3, i+1}:
#           return cnt
#         else:
#           next_set.add(i*2)
#           next_set.add(i*3)
#           next_set.add(i+1)
#         S = next_set

# print(get_min(N))