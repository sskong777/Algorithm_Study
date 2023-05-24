from collections import deque
import sys
input = sys.stdin.readline

t  = int(input())

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [2, 2, 1, -1, -2, -2, -1, 1]

def bfs():
    q = deque()
    q.append((sx,sy))

    while q:
        x, y = q.popleft()
        if x ==tx and y ==ty:
            return graph[x][y] -1
        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]
            if 0<=nx<l and 0<=ny<l and graph[nx][ny] == 0 :
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))

for test in range(t):
    l = int(input())
    graph = [[0]*l for _ in range(l)]
    sx,sy = map(int,input().split())
    tx, ty = map(int, input().split())
    graph[sx][sy] = 1
    print(bfs())