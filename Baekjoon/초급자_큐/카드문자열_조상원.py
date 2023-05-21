import sys

from collections import deque

input = sys.stdin.readline

n = int(input())

ret = []

for _ in range(n):
    t = int(input())
    d = deque(input().split())
    r = deque([])
    while d:
        c = d.popleft()
        if not r:
            r.append(c)
        else:
            if ord(c) <= ord(r[0]):
                r.appendleft(c)
            else:
                r.append(c)
    ret.append(''.join(r))

for t in ret:
    print(t)
