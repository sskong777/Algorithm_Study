# [1260] DFS와 BFS

# dfs 함수
def dfs(idx):   # idx라는 시작점에서 깊이 우선 탐색을 진행하는 함
    # visited가 전역 변수임을 나타내며, 이를 통해 함수 안에서도 visited를 수정할 수 있게 됩니다.
    global visited
    visited[idx] = True
    print(idx, end=' ')  # 출력 후 줄바꿈 대신 빈칸을 넣는 역할
    for next in range(1, N+1):
        # 다음 노드가 아직 방문되지 않고 and 그래프에서 현재 노드와 연결된 노드라면!
        # 그 노드를 시작점으로 하는 dfs를 재귀적으로 수행할 것이다.
        if not visited[next] and graph[idx][next]:
            dfs(next)

# bfs 함수


def bfs():
    global q, visited
    # 큐에 노드가 있을 동안 반복
    while q:
        cur = q.pop(0)  # 큐에서 가장 오래된 노드(=현재노드)를 pop하고 cur에 저장
        visited[cur] = True
        print(cur, end=' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                # 해당 노드를 방문했다는 것을 표시하고, 큐에 해당 노드를 추가한다
                # 다음 차례에 이 노드를 기준으로 인접한 노드들을 탐색하기 위함
                visited[next] = True
                q.append(next)


N, M, V = map(int, input().split())

# 2차원 배열의 graph
graph = [[False] * (N + 1) for _ in range(N+1)]
# 1차원 배열의 visitied(노드들의 방문 여부를 체크하는 리스트)
visited = [False] * (N + 1)

# 1. graph 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 2. dfs
dfs(V)
print()

# 3. bfs
visited = [False] * (N + 1)
q = [V]
visited[V] = True
bfs()
