# [2667] 단지번호 붙이기

# 아래 / 위 / 오른쪽 / 왼쪽
dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]


def dfs(y, x):
    global count
    visited[y][x] = True
    for dirIdx in range(4):
        ny = y + dirR[dirIdx]
        nx = x + dirC[dirIdx]
        if graph[ny][nx] and not visited[ny][nx]:
            count += 1
            dfs(ny, nx)


# 입력받기
N = int(input())
# graph
graph = [[0 for _ in range(N+2)]]
for _ in range(N):
    row = [0] + list(map(int, input().strip())) + [0]
    graph.append(row)
graph.append([0 for _ in range(N+2)])

# visited
visited = [[0] * (N+2) for _ in range(N+2)]


# 방문하지 않은 지점부터 dfs돌기
answers = []
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] and not visited[i][j]:
            count = 1
            dfs(i, j)
            answers.append(count)

answers.sort()
print(len(answers))
for answer in answers:
    print(answer)
