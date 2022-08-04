# 트리의 순회
import sys
sys.setrecursionlimit(10**8)
n = int(input())
inorder = input().split()
postorder = input().split()
position = [0]*(n+1)
for i in range(n):
  position[int(inorder[i])] =i

def conv(in_start, in_end, post_start, post_end):
  if in_end == in_start:
    return ' '+ inorder[in_start]
  else:
    root = postorder[post_end]
    indx = position[int(root)]
    if indx == in_start:
      return ' '+ root + conv(in_start+1, in_end, post_start, post_end-1)
    elif indx == in_end:
      return ' '+ root + conv(in_start, in_end-1, post_start, post_end-1)
    else:
      return ' '+root +conv(in_start, indx-1, post_start,  indx-1-in_start+post_start) + conv(indx+1, in_end, indx-in_start+post_start, post_end-1)

print(conv(0,len(inorder)-1, 0, len(inorder)-1).strip())
# def conv(instr, poststr):ㅋ
#   if len(instr) == 0:
#     return ''
#   elif len(instr) == 1:
#     return ' '+str(instr[0])
#   else:
#     mid = poststr[-1]
#     indx = instr.index(mid)
#     front_in = instr[0:indx]
#     back_in = instr[indx+1:]
#     front_post = poststr[0:indx]
#     back_post = poststr[indx: len(poststr)-1]
#     return ' '+str(mid) + conv(front_in, front_post) + conv(back_in, back_post)
# print(conv(inorder, postorder).strip())

