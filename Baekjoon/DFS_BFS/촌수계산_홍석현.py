def bfs(start):
    q = []
    q.append(start)

    while q:
        now = q.pop(0)
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = visited[now] + 1

N = int(input())
a, b = map(int,input().split())

M = int(input())
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
bfs(a)

if visited[b] == 0:
    print(-1)
else:
    print(visited[b])
