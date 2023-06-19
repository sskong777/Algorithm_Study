import sys
import math
import heapq
input = sys.stdin.readline

def dijkstra(k):
    dp[k] = 0
    queue = []
    heapq.heappush(queue, [0, k])
    
    while queue:
        cur_w, cur_v = heapq.heappop(queue)
        
        if dp[cur_v] < cur_w:
            continue
            
        for nv, nw in graph[cur_v]:
            temp = cur_w + nw
            if temp < dp[nv]:
                dp[nv] = temp
                heapq.heappush(queue, [temp, nv])

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
dp = [math.inf] * (n + 1)

for _ in range(m):
    a, b, c =  map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])
    
dijkstra(1)

print(dp[n])