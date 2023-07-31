def bfs(start, n, graph, visited):
    q = [start]
    visited[start] = 1
    cnt = 1
    while q:
        now = q.pop(0)
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1
                cnt += 1
    return cnt


def solution(n, wires):
    answer = 1e9
    graph = [[] for _ in range(n + 1)]
    # 그래프 입력 받기
    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    # 전선 하나씩 끊어서 비교
    for i in wires:
        graph[i[0]].remove(i[1])
        graph[i[1]].remove(i[0])

        # bfs
        compare = []
        visited = [0] * (n + 1)

        for j in range(1, n + 1):
            if not visited[j]:
                cnt = bfs(j, n, graph, visited)
                compare.append(cnt)

        # 두 전력망의 차 => 최소값 갱신
        answer = min(answer, abs(compare[0] - compare[1]))
        # 원래대로 초기화
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    return answer