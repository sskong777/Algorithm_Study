from collections import deque

def solution(maps):
    row = len(maps)  # 행
    col = len(maps[0])  # 열

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:  # 행 / 열
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    if maps[row - 1][col - 1] == 1:
        return -1
    else:
        return maps[row - 1][col - 1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))