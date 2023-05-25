import sys


def dfs(v):
    visited[v] = True
    for i in li[v]:
        if not visited[i]:
            dfs(i)


input = sys.stdin.readline


n = int(input())
m = int(input())

li = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    li[x].append(y)
    li[y].append(x)

for i in li:
    i.sort()

visited = [False] * (n+1)
dfs(1)
print(sum(visited)-1)