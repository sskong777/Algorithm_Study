from collections import deque
import sys

input = sys.stdin.readline

n, k, m = map(int, input().split())
d = deque([i for i in range(1, n+1)])
ret = []
c = 0
while d:
    d.rotate(-(k-1))
    ret.append(d.popleft())
    c += 1
    if c == m:
        d.reverse()
        c = 0
for t in ret:
    print(t)