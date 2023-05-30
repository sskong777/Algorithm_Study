computer = int(input())
link = int(input())

network = [[] * computer for _ in range(computer + 1)]
visited = [False] * (computer + 1)

for i in range(link):
    p, c = map(int, input().split())
    network[p].append(c)
    network[c].append(p)

cnt = 0


def dfs(cur):
    global cnt
    visited[cur] = True

    for next in network[cur]:
        if not visited[next]:
            cnt += 1
            dfs(next)


dfs(1)
print(cnt)
