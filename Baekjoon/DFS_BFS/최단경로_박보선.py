import sys
import math
import heapq
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
dp = [math.inf] * (v + 1)

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
            
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

dijkstra(k)
for i in range(1, v + 1):
    if dp[i] == math.inf:
        print('INF')
    else:
        print(dp[i])