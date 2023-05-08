import sys
from collections import deque
input = sys.stdin.readline

def bfs(v:list[bool], g:list[list]) -> None:
    v[1] = True
    queue = deque(g[1])
    while queue:
        cur = queue.popleft()
        
        if v[cur] == False:
            v[cur] = True
            if len(g[cur]) != 0:
                queue.extend(g[cur])

n = int(input())
m = int(input())

virus = [False for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(virus, graph)

print(virus.count(True)-1)