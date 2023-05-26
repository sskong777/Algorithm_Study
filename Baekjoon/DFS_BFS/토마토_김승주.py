from collections import deque
import sys
input = sys.stdin.readline 

dx = [ 1, 0, -1, 0]
dy = [ 0, 1, 0, -1]


def bfs():
    while q :
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and tomato_box[nx][ny] ==0:
                tomato_box[nx][ny] = tomato_box[x][y] +1
                q.append((nx,ny))


m, n  = map(int, input().split())

tomato_box = []
q = deque([])

for i in range(n):
    tomato_box.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if tomato_box[i][j]==1:
            q.append((i,j))

bfs()

result = 0
for i in range(n):
    for j in range(m):
        if tomato_box[i][j] == 0 :
            print(-1)
            exit()
    result = max(result,max(tomato_box[i]))
print(result-1)