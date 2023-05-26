import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(t)]
ret = []


def bfs(r, c):
    q = deque([(r, c)])
    graph[r][c] = 0
    cnt = 1
    while q:
        r, c = q.popleft()
        for i, j in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = r+i, c+j
            if 0 <= nr < len(graph) and 0 <= nc < len(graph[0]):
                if graph[nr][nc] == 1:
                    q.append((nr, nc))
                    graph[nr][nc] = 0
                    cnt += 1
    return cnt


for r in range(len(graph)):
    for c in range(len(graph[0])):
        if graph[r][c] == 1:
            cnt = bfs(r, c)
            ret.append(cnt)

print(len(ret))
ret.sort()
for i in ret:
    print(i)
