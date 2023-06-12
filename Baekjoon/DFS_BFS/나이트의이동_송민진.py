import sys
from collections import deque
input = sys.stdin.readline

dx = [-2, -1, 1, 2,  2,  1, -1, -2]
dy = [ 1,  2, 2, 1, -1, -2, -2, -1]

tc = int(input())
for _ in range(tc):
    def solution():
        l = int(input())
        now_x, now_y = map(int, (input().strip().split()))
        target_x, target_y = map(int, input().strip().split())

        board = [[0] * l for _ in range(l)]
        board[now_x][now_y] = 1

        if now_x == target_x and now_y == target_y:
            return 0

        else:
            q = deque([(now_x, now_y)])
            while q:
                x, y = q.popleft()
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < l and 0 <= ny < l and board[nx][ny] == 0:
                        board[nx][ny] = board[x][y] + 1
                        if nx == target_x and ny == target_y:
                            return board[nx][ny] -1
                        q.append((nx, ny))

    print(solution())