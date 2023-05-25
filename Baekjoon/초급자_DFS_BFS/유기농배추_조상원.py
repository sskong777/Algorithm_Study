import sys

input = sys.stdin.readline

t = int(input())

ret = []


def bfs(r, c):
    q = [(r, c)]
    while q:
        r, c = q.pop(0)
        for i, j in [(-1, 0), (0, - 1), (1, 0), (0, 1)]:
            if 0 <= r+i < len(graph) and 0 <= c+j < len(graph[0]):
                if graph[r+i][c+j] == 1:
                    graph[r+i][c+j] = 0
                    q.append((r+i, c+j))


for _ in range(t):
    m, n, c = map(int, input().split())
    graph = [[0] * (n) for _ in range(m)]

    for _ in range(c):
        r, c = map(int, input().split())
        graph[r][c] = 1

    visited = set()
    cnt = 0
    for r in range(len(graph)):
        for c in range(len(graph[0])):
            if graph[r][c] == 1:
                bfs(r, c)
                cnt += 1
    ret.append(cnt)


for t in ret:
    print(t)
