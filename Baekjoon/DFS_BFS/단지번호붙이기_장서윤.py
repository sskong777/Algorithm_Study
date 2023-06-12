from collections import deque

n = int(input())

que = deque()

Map = []

visited = [[False] * n for _ in range(n)]

for i in range(n):
    Map.append(list(map(int, input())))


def bfs(px, py):
    cnt = 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    que.append([px, py])
    visited[px][py] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if -1 < nx < n and -1 < ny < n and Map[nx][ny] and not visited[nx][ny]:
                que.append([nx, ny])
                cnt += 1
                visited[nx][ny] = True
    return cnt


ans = []
for px in range(n):
    for py in range(n):
        if not visited[px][py] and Map[px][py]:
            ans.append(bfs(px, py))

print(len(ans))
ans.sort()
for i in ans:
    print(i)
