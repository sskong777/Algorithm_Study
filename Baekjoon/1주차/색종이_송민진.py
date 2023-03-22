import sys
input = sys.stdin.readline
board = [[False for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    x, y = map(int, input().strip().split())
    for row in range(10):
        board[x+row][y:y+10] = [True] * 10

cnt = 0
for k in range(100):
    cnt += board[k].count(True)

print(cnt)