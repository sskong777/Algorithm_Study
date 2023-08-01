result = 0


def dfs(graph, visited, n):
    global result

    visited[n] = True
    result += 1  # 연결된 노드 카운트

    for i in graph[n]:  # 그래프에 연결된 노드 하나씩 방문
        if not visited[i]:
            dfs(graph, visited, i)


def solution(n, wires):
    global result
    answer = 101
    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for wire in wires:  # 그래프 구성
        f, s = wire
        graph[f].append(s)
        graph[s].append(f)

    for wire in wires:
        # 연결 하나씩 끊어가면서 dfs 실행
        f, s = wire
        graph[f].remove(s)
        graph[s].remove(f)

        dfs(graph, visited, 1)

        # 첫 번째 그룹만 카운팅 하고 나머지 그룹은 n개에서 빼서 계산해줌
        a, b = result, abs(n - result)
        answer = min(abs(a - b), answer)

        # 다시 원래대로 돌려줌
        visited = [False] * (n + 1)
        graph[f].append(s)
        graph[s].append(f)
        result = 0

    return answer
