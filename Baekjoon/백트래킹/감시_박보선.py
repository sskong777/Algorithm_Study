import sys
import copy
input = sys.stdin.readline

board = []
cctv = []

mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

#    북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


n, m = map(int, input().split())

for i in range(n):
    board.append(list(map(int, input().split())))
    
    for j in range(m):
        if board[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([board[i][j], i, j])

def dfs(d, b):
    global min_val
    
    if d == len(cctv):
        count = 0
        for i in range(n):
            count += b[i].count(0)
        
        min_val = min(min_val, count)
        return

    temp = copy.deepcopy(b)
    c, x, y = cctv[d]
    for i in mode[c]:
        fill(temp, i, x, y)
        dfs(d + 1, temp)
        temp = copy.deepcopy(b)

def fill(b, mm, x, y):
    for i in mm:
        nx = x
        ny = y
        
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m or b[nx][ny] == 6:
                break
            elif b[nx][ny] == 0:
                b[nx][ny] = '#'

min_val = int(1e9)
dfs(0, board)
print(min_val)