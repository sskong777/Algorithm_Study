import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
square = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(n+1)]
visited = square
arr = []

for _ in range(m):
    i, j, k = map(int, input().strip().split())
    square[i][j][k] = 1
    arr.append([i, j, k])

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def check(x, y, z):
    cnt = 0
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 1 <= nx <= n and 1 <= ny <= n and  1 <= nz <= n and square[nx][ny][nz] == 1:
            cnt += 1
        else:
            break
    if cnt == 6:
        return True
    else:
        return False

answer = 0
for i, j, k in arr:
    if check(i, j, k):
        answer += 1


print(answer)