import sys

N = int(sys.stdin.readline().strip())
deck = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
card = list(map(int, sys.stdin.readline().split()))

deck.sort()

def find_card(n):
    start = 0
    