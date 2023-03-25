import sys
input = sys.stdin.readline

board = []
for _ in range(10):
    board.append(list(input().strip()))

def omok_check(x, y):

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    for d in range(8):
        cnt = 1 if board[x][y] == "X" else 0
        empty_cnt = 1 if board[x][y] == "." else 0
        now_x, now_y = x, y

        for _ in range(4):
            nx = now_x + dx[d]
            ny = now_y + dy[d]

            if 0 <= nx < 10 and 0 <= ny < 10:
                if board[nx][ny] == "X":
                    cnt += 1
                elif board[nx][ny] == ".":
                    empty_cnt += 1
            else:
                break
            if empty_cnt > 1:
                break
            now_x = nx
            now_y = ny
        if (cnt >= 4 and empty_cnt == 1) or (cnt >= 5 and empty_cnt == 0):
            return True
    return False

def solution():
    for i in range(10):
        for j in range(10):
            if omok_check(i, j):
                return 1
    return 0

print(solution())