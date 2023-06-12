# [18352] 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

import sys
from collections import deque

N, M, K, X = map(int, input().split())
MAP = {}
for l in sys.stdin.read().strip().split('\n'):
    from_, to = map(int, l.split())
    MAP.setdefault(from_, []).append(to)

dist = [300001]*(N+1)
dq = deque([(X, 0)])
while dq:
    node, d = dq.popleft()
    if node not in MAP: continue
    for t in MAP[node]:
        if d < dist[t]:
            dq.append((t, d+1))
            dist[t] = d+1

cities = [str(i) for i in range(1, N+1) if dist[i] == K and i != X]
print("\n".join(cities) if cities else "-1")