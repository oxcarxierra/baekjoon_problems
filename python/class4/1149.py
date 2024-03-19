# RGB 거리

N = int(input())
min_arr = [[0,0,0]]
for i in range(1,N+1):
  r, g, b = map(int, input().split())
  min_arr.append([r+min(min_arr[i-1][1],min_arr[i-1][2]),g+min(min_arr[i-1][0],min_arr[i-1][2]),b+min(min_arr[i-1][1],min_arr[i-1][0])])
print(min(min_arr[N]))