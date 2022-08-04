# 용액

N = int(input())
sol = list(map(int, input().split()))

def neutralize():
  pl, pr = 0, N-1
  minimum = [sol[pl], sol[pr]]
  while pl != pr:
    x = sol[pr] + sol[pl]
    if x == 0:
      print(sol[pl], sol[pr], sep=' ')
      return
    if abs(x) < abs(sum(minimum)):
      minimum = [sol[pl], sol[pr]]
    if x > 0:
      pr -= 1
    elif x<0:
      pl += 1
  print(minimum[0], minimum[1], sep=' ')

neutralize()