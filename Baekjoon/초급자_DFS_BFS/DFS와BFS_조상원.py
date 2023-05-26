import sys
from collections import deque

input = sys.stdin.readline
n, m, s = map(int, input().split())

graph = [[False] * (n+1) for _ in range(n+1)]

for _ in range(m):
    b, e = map(int, input().split())
    graph[b][e] = True
    graph[e][b] = True

visited = set()
ret = []


def bfs(v):
    q = deque([v])
    visited.add(v)
    while q:
        c = q.popleft()
        ret.append(c)
        for i in range(1, n+1):
            if i not in visited and graph[c][i]:
                q.append(i)
                visited.add(i)


def dfs(v):
    visited.add(v)
    ret.append(v)
    for i in range(1, n+1):
        if i not in visited and graph[v][i]:
            dfs(i)


dfs(s)
print(*ret)
visited = set()
ret = []
bfs(s)

print(*ret)
