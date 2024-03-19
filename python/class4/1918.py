# 후위 표기식

eq = input().strip()
posteq = ''
opstack = []
opdic={'(':1, '+':2, '-':2, '*':3, '/':3}
for i in eq:
  if i.isalpha():
    posteq += i
  elif i=='(':
    opstack.append(i)
  elif i==')':
    while opstack:
      operator = opstack.pop()
      if operator == '(':
        break
      posteq += operator
  else:
    while opstack and opdic[opstack[-1]] >= opdic[i]:
      posteq += opstack.pop()
    opstack.append(i)
while opstack:
  posteq += opstack.pop()
print(posteq)