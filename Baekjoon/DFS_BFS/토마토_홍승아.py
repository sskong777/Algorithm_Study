# [7576] 토마토
import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
boxes = []
for i in range(n):
    boxes.append(list(map(int, input().split())))

# for i in range(n):
#     print(boxes[i])

queue = deque()
cnt = 0
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            cnt += 1
            queue.append([i, j])

if cnt == m*n:
    print(0)
    exit(0)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if boxes[nx][ny] == 0:
                boxes[nx][ny] = boxes[x][y] + 1
                queue.append([nx,ny])

ans = 0
for i in range(n):
    for j in range(m):
        if boxes[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(boxes[i]))

print(ans-1)