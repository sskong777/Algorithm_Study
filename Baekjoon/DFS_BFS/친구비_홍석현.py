def bfs(start):
    q = []
    q.append(start)
    visited[start] = 1
    charge = [arr[start-1]]
    while q:
        now = q.pop(0)
        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = 1
                charge.append(arr[next-1])

    return charge

N, M, k = map(int,input().split())
arr = list(map(int,input().split()))
graph = [[]*(N+1) for _ in range(N+1)]
visited = [0] * (N+1)

for i in range(M):
    v,w = map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)

ans = 0
for i in range(1,N+1):
    if not visited[i]:
        charge = bfs(i)
        ans += min(charge)

if ans > k:
    print("Oh no")
else:
    print(ans)
