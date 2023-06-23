import itertools
import sys
from collections import deque

R, C = map(int, input().split())
M = sys.stdin.read().strip().split('\n')
vector = [(0,1), (1,0), (0,-1), (-1,0)]

def bfs(r, c):
    _max = 0
    dq = deque([(r, c, 0)])
    visited=[[0]*C for _ in range(R)]
    visited[r][c] = 1
    while dq:
        r, c, d = dq.popleft()
        _max = max(d, _max)
        for dr, dc in vector:
            nr, nc = r+dr, c+dc
            if (0 <= nr < R and 0 <= nc < C
                and M[nr][nc] == "L" 
                and not visited[nr][nc]):
                visited[nr][nc] = 1
                dq.append((nr, nc, d+1))
    return _max


ans = 0
for r, c in itertools.product(range(R), range(C)):
    if M[r][c] == "W": continue
    ans = max(ans, bfs(r, c))
print(ans)