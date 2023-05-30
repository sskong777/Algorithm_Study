import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input().strip()))))

answer = []

q = deque([])
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(start):
    q.append(start)
    cnt = 1
    graph[start[0]][start[1]] = 0
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1

    answer.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            bfs((i, j))

print(len(answer))
answer.sort()
for ans in answer:
    print(ans)