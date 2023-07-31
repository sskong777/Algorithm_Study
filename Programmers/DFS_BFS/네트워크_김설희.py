def solution(n, computers):

    connections = [[] for _ in range(n)]
    visited = [0] * n

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                if j not in connections[i]:
                    connections[i].append(j)
                if i not in connections[j]:
                    connections[j].append(i)

    def dfs(v):
        visited[v] = 1
        for i in connections[v]:
            if visited[i] == 0:
                dfs(i)

    cnt = 1
    dfs(0)

    while True:
        if 0 in visited:
            dfs(visited.index(0))
            cnt += 1
        else:
            return cnt


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))