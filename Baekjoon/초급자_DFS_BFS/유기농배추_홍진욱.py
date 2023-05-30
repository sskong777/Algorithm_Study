import sys

sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        field[Y][X] = 1

    count = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        field[y][x] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < M and 0 <= ny < N and field[ny][nx] == 1:
                dfs(nx, ny)

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                dfs(j, i)
                count += 1
    print(count)
