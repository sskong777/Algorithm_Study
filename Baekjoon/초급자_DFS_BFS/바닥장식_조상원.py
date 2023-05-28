import sys

input = sys.stdin.readline

n, m = map(int, input().split())


visited = set()

graph = [list(input()) for _ in range(n)]
cnt = 0


def dfs(r, c):
    visited.add((r, c))
    if graph[r][c] == '|':
        nr = r+1
        if nr < n and graph[nr][c] == '|' and (nr, c) not in visited:
            dfs(nr, c)
        return
    if graph[r][c] == '-':
        nc = c+1
        if nc < m and graph[r][nc] == '-' and (r, nc) not in visited:
            dfs(r, nc)
        return


for r in range(n):
    for c in range(m):
        if (r, c) not in visited:
            dfs(r, c)
            cnt += 1

print(cnt)
