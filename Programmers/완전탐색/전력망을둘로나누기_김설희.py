def solution(n, wires):

    result = []

    for i in range(len(wires)):
        copy_wires = wires.copy()
        copy_wires.pop(i)
        g = [[] for i in range(n + 1)]
        visited = [0] * (n + 1)

        for wire in copy_wires:
            a, b = wire
            g[a].append(b)
            g[b].append(a)

        def dfs(v):
            visited[v] = 1
            for i in g[v]:
                if visited[i] == 0:
                    dfs(i)

        dfs(1)

        result.append(abs(sum(visited) - (n - sum(visited))))

    return min(result)

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))