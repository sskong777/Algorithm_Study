import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, d = map(int, input().strip().split())
graph = [[] for _ in range(d+1)]    # 연결 점 정보
distance = [INF] * (d+1)

for i in range(d+1):
    graph[i].append((i+1, 1))

for _ in range(n):
    start, end, length = map(int, input().strip().split())
    if end <= d:
        graph[start].append((end, length))

def dijkstra():
    pq = []
    heapq.heappush(pq, (0, 0))      # (거리, 출발점)

    while pq:
        dist, now = heapq.heappop(pq)
        if now <= d and distance[now] < dist:
            continue

        for node in graph[now]:
            cost = dist + node[1]
            if node[0] <= d and cost < distance[node[0]]:
                distance[node[0]] = cost
                heapq.heappush(pq, (cost, node[0]))


dijkstra()

print(distance[d])
