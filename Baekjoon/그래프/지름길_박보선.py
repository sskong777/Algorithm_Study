import sys
import heapq
input = sys.stdin.readline


n, d = map(int, input().split())

graph = [[] for _ in range(d + 1)]
dis = [int(1e9)] * (d + 1)
dis[0] = 0

for i in range(d):
    graph[i].append((i + 1, 1))

for i in range(n):
    s, e, l = map(int, input().split())

    if e <= d:
        graph[s].append((e, l))
        
queue = []
heapq.heappush(queue, (0, 0))

while queue:
    end, length = heapq.heappop(queue)
    
    if end > dis[length]:
        continue
    
    for g in graph[length]:
        c = end + g[1]
        if c < dis[g[0]]:
            dis[g[0]] = c
            heapq.heappush(queue, (c, g[0]))

print(dis[d])