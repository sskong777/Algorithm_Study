# [2606] 바이러스

def dfs(idx):
    global answer
    visited[idx] = True
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:
            answer += 1
            dfs(next)


# 입력받기
N = int(input())
C = int(input())
answer = 0

# graph
graph = [[False] * (N+1) for _ in range(N+1)]
# visited
visited = [False] * (N+1)


for i in range(C):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 1. dfs로 구현
dfs(1)
print(answer)
