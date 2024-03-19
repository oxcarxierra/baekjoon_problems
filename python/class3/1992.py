# 쿼드트리

import sys
N = int(sys.stdin.readline())
image = []
for _ in range(N):
  row = sys.stdin.readline().strip()
  image.append(list(row[i] for i in range(N)))
print(image)

def quadtree(x, y, n):
  for dx in range(n):
    for dy in range(n):
      if not image[x+dx][y+dy] == image[x][y]:
          return '('+quadtree(x, y, n//2)+quadtree(x, y+n//2, n//2)+quadtree(x+n//2, y, n//2)+quadtree(x+n//2, y+n//2, n//2)+')'
  return image[x][y]

print(quadtree(0,0,N))


