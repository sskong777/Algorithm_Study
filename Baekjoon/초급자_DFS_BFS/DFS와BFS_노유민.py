import sys
from collections import deque


def dfs(v):
    visited[v] = True
    print(v, end=" ")

    for i in li[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        x = q.popleft()
        print(x, end=" ")

        for i in li[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


input = sys.stdin.readline

n, m, v = map(int, input().split())

li = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    li[x].append(y)
    li[y].append(x)

for i in li:
    i.sort()

visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)
