import sys

N = int(sys.stdin.readline().strip())
deck = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
card = list(map(int, sys.stdin.readline().split()))

hash = {}
for i in deck:
    if i in hash:
        hash[i] += 1
    else: 
        hash[i] = 1
answer = []
for i in card:
    if i in hash:
        answer.append(str(hash[i]))
    else:
        answer.append('0')
print(' '.join(answer))

#이분탐색으로 접근 - 실패
# deck.sort()
# def find_card(n):
#     start = 0
#     end = N-1
#     while start <= end :
#         p = (start + end) // 2
#         if deck[p] > n:
#             end = p - 1
#         elif deck[p] < n :
#             start = p + 1
#         elif deck[p] == n:
#             cnt = 1
#             i, j=1, 1
#             while p-i>= 0:
#                 if deck[p-i] == n:
#                     cnt += 1
#                     i += 1
#                 else:
#                     break
#             while p+j < N:
#                 if deck[p+j] == n:
#                     cnt += 1
#                     j += 1
#                 else: 
#                     break
#             return cnt
#     return 0

# answer = []
# for i in range(M): 
#     answer.append(str(find_card(card[i])))

# print(' '.join(answer))