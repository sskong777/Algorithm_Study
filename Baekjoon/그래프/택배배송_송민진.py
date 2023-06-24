import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().strip().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
def dijkstra(start):
    heapq.heappush(q, (0, start))
    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for conn in graph[now]:
            node, cost = conn[0], conn[1]
            new_cost = cost + d
            if new_cost < distance[node]:
                distance[node] = new_cost
                heapq.heappush(q, (new_cost, node))

dijkstra(1)
print(distance[n])