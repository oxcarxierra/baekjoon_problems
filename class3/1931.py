# 회의실 배정
# 그리디 알고리즘, 탐욕법

import sys
N = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
cnt = 1
time.sort(key=lambda t: (t[1],t[0]))
end_time = time[0][1]
for i in range(1,N):
  if time[i][0] >= end_time:
    cnt += 1
    end_time=time[i][1]
# print(cnt)
# def greedy():
#   global cnt, time
#   time_min = time[0]
#   new_time=[]
#   for i in time:
#     if not time_min[1]<=i[0]:
#       new_time.append(i)
#   # print(new_time)
#   time=new_time
#   print(time)
#   cnt += 1
#   if time:
#     greedy()
#   else:
#     print(cnt)

# greedy()