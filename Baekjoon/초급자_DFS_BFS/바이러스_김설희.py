import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]
    graph[b] += [a]
    # graph의 인덱스가 컴퓨터의 번호!

def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
print(sum(visited)-1)