# LCS 

A = input()
B = input()
n, m = len(A),len(B)

LCS = [[0]*(m+1)for _ in range(n+1)]
for i in range(1,m+1):
  for j in range(1, n+1):
    if A[j-1] == B[i-1]:
      LCS[j][i] = LCS[j-1][i-1] + 1
    else:
      LCS[j][i] = max(LCS[j-1][i], LCS[j][i-1])
print(LCS[n][m])
