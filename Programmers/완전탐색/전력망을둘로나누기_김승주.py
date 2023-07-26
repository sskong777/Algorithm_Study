# 초기 세팅이 하나의 트리로 연결되어 있고 이중 하나를 끊어서 둘로 만든 것
# 그러면 끊긴 간선의 v1, v2가 다른 그룹에 속하게 되므로 각각  개수 count 하는 bfs 돌면 됨!
# union 써도 될 거 같은데 -> 이 부분 공부해서 다른 풀이로도 풀어볼 것
from collections import deque


def solution(n, wires):
    answer = -1

    graph = [[] for _ in range(n+1)]

    for v1, v2 in wires:  # 양방향이랍니다!
        graph[v1].append(v2)
        graph[v2].append(v1)

    min_diff = 1e9

    def bfs(start):
        visited = [False] * (n+1)
        visited[start] = True
        q = deque()
        q.append(start)

        count = 1
        while q:
            x = q.popleft()

            for nx in graph[x]:
                if visited[nx] == False:  # 아직 방문하지 않은 노드 이면
                    visited[nx] = True
                    count += 1
                    q.append(nx)
        return count

    for v1, v2 in wires:
        graph[v1].remove(v2)  # 해당 연결 지우기
        graph[v2].remove(v1)
        min_diff = min(abs(bfs(v1)-bfs(v2)), min_diff)    # abs 때려야해요!
        graph[v1].append(v2)  # 연결 다시 넣기
        graph[v2].append(v1)

    return min_diff
