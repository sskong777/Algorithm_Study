# [1012] 유기농 배추
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
Max = 52

# 아래 / 위 / 오른쪽 / 왼쪽 : range(4)인 이유
dirR = [1, -1, 0, 0]  # 상,하 이동을 위한 값
dirC = [0, 0, 1, -1]  # 좌,우 이동을 위한 값

# 아래의 for문은 현재 위치로부터 상,하,좌,우를 탐색
for dirIdx in range(4):
    newY = y + dirR[dirIdx]  # 다음에 탐색할 세로 좌표 계산
    newX = x + dirC[dirIdx]  # 다음에 탐색할 가로 좌표 계산
    # 탐색할 위치에 배추가 있고, 아직 방문하지 않았다면 다시 dfs를 호출
    if graph[newY][newX]
    dfs(newY, newX)  # 다음 위치에서 다시 dfs를 시작


T = int(input())
for _ in range(T):
    # 가로, 세로, 배추위치개수
    M, N, K = map(int, input().split())
    graph = [[False] * Max for _ in range(Max)]
    visited = [[False] * Max for _ in range(Max)]

    # graph 정보 입렫
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = True

count = []
for y in range(1, N + 1):
    for x in range(1, N + 1):
        if graph[y][x]:
            count.append(dfs(x, y), count=1)
