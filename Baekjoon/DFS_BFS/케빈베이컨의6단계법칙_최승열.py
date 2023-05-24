# [1389] 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys
from collections import deque
N, M = map(int, input().split())

MAP = {}
dist = [[200]*(101) for _ in range(101)]

for l in sys.stdin.read().strip().split('\n'):
    a, b = map(int, l.split())
    MAP.setdefault(a, []).append(b)
    MAP.setdefault(b, []).append(a)

dq = deque()

def bfs(start):
    while dq:
        node, d = dq.popleft()
        for t in MAP[node]:
            if dist[start][t] >= d+1:
                dq.append((t, d+1))
                dist[start][t] = dist[t][start] = d+1
                
def get_kebin(num):
    t = 0
    for i in MAP.keys():
        t += dist[num][i]
    return t - dist[num][num]

for j in MAP.keys():    
    dq.append((j, 0))
    bfs(j)
    dq.clear()

kebin = [200] * (101)
for j in MAP.keys():  
    kebin[j] = get_kebin(j)
    
print(kebin.index(min(kebin)))
