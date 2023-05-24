# # 시도 1
# from collections import deque
# import sys
# input = sys.stdin.readline
#
#
# m, n = map(int, input().strip().split())
# box = []
# # visited = [[False] * n for _ in range(m)]
#
# day_cnt = 0
# visited_zero_cnt = 0
# zero_cnt = 0
# for _ in range(n):
#     line = list(map(int, input().strip().split()))
#     box.append(line)
#     zero_cnt += line.count(0)
#
# q = deque([])
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# def bfs(start):
#     global visited_zero_cnt
#     q.append(start)
#     while q:
#         x, y = q.popleft()
#         if box[x][y] == 0:
#             visited_zero_cnt += 1
#         box[x][y] = -1
#         for di in range(4):
#             nx, ny = x + dx[di], y + dy[di]
#             if 0 <= nx < m and 0 <= ny < n and box[nx][ny] == 0:
#                 q.append((nx, ny))
#                 visited_zero_cnt += 1
#                 # visited[nx][ny] = True
#
#
#
# for i in range(m):
#     for j in range(n):
#         if box[i][j] != -1:
#             bfs((i, j))
#
# if visited_zero_cnt != zero_cnt:
#     print(-1)

# 시도 2
from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().strip().split())
box = []

for _ in range(n):
    line = list(map(int, input().strip().split()))
    box.append(line)

q = deque([])

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs():
    while q:
        x, y = q.popleft()
        for di in range(4):
            nx, ny = x + dx[di], y + dy[di]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                q.append((nx, ny))
                if box[nx][ny] == 0 or box[nx][ny] > box[x][y] + 1:
                    box[nx][ny] = box[x][y] + 1

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

bfs()

def make_answer():
    max_value = 0
    for a in range(n):
        for b in range(m):
            if box[a][b] == 0:
                return -1
            max_value = max(max_value, box[a][b])
    return max_value-1

print(make_answer())