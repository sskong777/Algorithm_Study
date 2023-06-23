import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().strip().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    start, end, length = map(int, input().strip().split())
    if end <= d:
        graph[start].append((end, length))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        d, now = heapq.heappop(q)
        if distance[now] < d:
            continue
        for conn in graph[now]:
            cost = d + conn[1]
            if cost < distance[conn[0]]:
                distance[conn[0]] = cost
                heapq.heappush(q, (cost, conn[0]))

dijkstra(0)

print(distance[d])