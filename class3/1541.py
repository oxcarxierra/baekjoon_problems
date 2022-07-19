# 잃어버린 괄호

import sys
equation = sys.stdin.readline().strip().replace('-','+-')
numbers = equation.split('+')
sum, threshold=0, len(numbers)
for i in range(len(numbers)):
  if numbers[i][0] == '-':
    threshold = i
    break
for i in range(len(numbers)):
  number = int(numbers[i][1:]) if numbers[i][0] == '-' else int(numbers[i])
  if i < threshold:
    sum += number
  else:
    sum -= number
print(sum)