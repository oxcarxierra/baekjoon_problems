# 선분 교차 2

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def cross():
  if (y2-y1)*(x4-x3) == (y4-y3)*(x2-x1): #기울기 동일
    if (y3-y1)(x2-x1) == (y2-y1)(x3-x1): # y절편 동일
      if max(x1,x2) < min(x3,x4) or max(x3,x4) < min(x1,x2): # 교점 없을 조건
        return 0
      else:
        return 1
    else:
      return 0 # 평행한데 만날 일 없는 상황
  else:
