from collections import deque

computer = int(input())
network = int(input())

graph = [[] * computer for _ in range(computer + 1)]
visited = [False] * (computer + 1)
q = deque()

for i in range(network):
    first, second = map(int, input().split())
    graph[first].append(second)
    graph[second].append(first)


def bfs(start):
    ans = 0
    q.append(start)
    visited[start] = True

    while q:
        f_node = q.popleft()

        for s_node in graph[f_node]:
            if not visited[s_node]:
                q.append(s_node)
                visited[s_node] = True
                ans += 1
    return ans


print(bfs(1))
