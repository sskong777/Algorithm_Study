n = int(input())
s, e = map(int, input().split())
m = int(input())

graph = [[] * n for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

ans = 0


def dfs(p, cnt):
    global ans
    if e == p:
        ans = cnt
        return

    visited[p] = True

    for next in graph[p]:
        if not visited[next]:
            dfs(next, cnt+1)


dfs(s, 0)
if ans == 0:
    print(-1)
else:
    print(ans)
