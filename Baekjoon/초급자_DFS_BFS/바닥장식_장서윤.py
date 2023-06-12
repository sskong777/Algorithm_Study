from collections import deque

n, m = map(int, input().split())

Map = list()
que = deque()

visited = [[False] * m for _ in range(n)]

for i in range(n):
    Map.append(list(input()))

d = [-1, 1]

ans = 0


def dfs(y, x):
    visited[y][x] = True

    for i in range(2):
        if Map[y][x] == '-':
            nx = x + d[i]
            ny = y + 0
        if Map[y][x] == '|':
            nx = x + 0
            ny = y + d[i]

        if 0 <= nx < m and 0 <= ny < n and not visited[ny][nx]:
            if Map[ny][nx] == Map[y][x]:
                dfs(ny, nx)


for y in range(n):
    for x in range(m):
        if not visited[y][x]:
            dfs(y, x)
            ans += 1
dfs(0, 0)
print(ans)
