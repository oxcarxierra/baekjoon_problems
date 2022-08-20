import sys

def findroom(H, W, N):
    room = [1,1]
    for _ in range(N-1):
        if (room[0] == H):
                newroom = [1, room[1]+1]
        else:
            newroom = [room[0]+1, room[1]]
        room = newroom
    return room

T = int(sys.stdin.readline().strip())
for _ in range(T):
    H, W, N = map(int, sys.stdin.readline().split())
    room = findroom(H, W, N)
    print(room[0]*100+room[1])