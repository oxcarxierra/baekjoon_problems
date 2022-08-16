#내려가기

n = int(input())
min_dp = [0,0,0]
max_dp = [0,0,0]
for _ in range(n):
  row = list(map(int, input().split()))
  new_max = [0,0,0]
  new_max[0] = row[0] + max(max_dp[0], max_dp[1])
  new_max[1] += row[1] + max(max_dp)
  new_max[2] +=row[2] + max(max_dp[1], max_dp[2])
  max_dp = new_max
  new_min = [0,0,0]
  new_min[0] = row[0] + min(min_dp[0], min_dp[1])
  new_min[1] += row[1] + min(min_dp)
  new_min[2] +=row[2] + min(min_dp[1], min_dp[2])
  min_dp = new_min

print(max(max_dp), end=' ')
print(min(min_dp))

