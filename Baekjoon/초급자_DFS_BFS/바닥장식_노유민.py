import sys

input = sys.stdin.readline


def dfs(x, y):
    if graph[x][y] == '-':
        graph[x][y] = 'True'
        for i in [1, -1]:
            y += i
            if y > 0 and y < m and graph[x][y] == '-':
                dfs(x, y)

    if graph[x][y] == '|':
        graph[x][y] = 'True'
        for i in [1, -1]:
            x += i
            if x > 0 and x < n and graph[x][y] == '|':
                dfs(x, y)


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
count = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-' or graph[i][j] == '|':
            dfs(i, j)
            count += 1
print(count)
