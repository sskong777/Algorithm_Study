n = int(input())
start, end = map(int, input().split())
m = int(input())

graph = [[] * n for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def dfs(start, tmp):
    global ans, status

    visited[start] = True

    if start == end:
        ans = tmp
        status = True
        return status

    for y in graph[start]:
        if not visited[y]:
            dfs(y, tmp + 1)

status = False
ans = 0

dfs(start, 0)
if status:
    print(ans)
else:
    print(-1)
