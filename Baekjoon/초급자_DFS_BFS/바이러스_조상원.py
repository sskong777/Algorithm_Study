import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())

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


bfs(1)
print(len(ret)-1)