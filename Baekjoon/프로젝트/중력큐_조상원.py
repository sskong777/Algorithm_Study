import sys

from collections import deque
input = sys.stdin.readline

n = int(input())

q = deque([])
ret = []


state = 1

b = 0
w = 0

for _ in range(n):
    com = input().split()
    if len(com) == 1:
        if len(q) != 0:
            h = q.popleft()
            if h == 'b':
                b -= 1
            elif h == 'w':
                w -= 1
    else:
        c, t = com
        if c == 'push':
            q.append(t)
            if t == 'b':
                b += 1
            elif t == 'w':
                w += 1
        elif c == 'count':
            if t == 'b':
                ret.append(b)
            elif t == 'w':
                ret.append(w)
        elif c == 'rotate':
            if t == 'l':
                state = state - 1 if state > 1 else 4
            elif t == 'r':
                state = state + 1 if state < 4 else 1
    if state == 2:
        while q and q[0] != 'w':
            q.popleft()
            b -= 1
    elif state == 4:
        while q and q[-1] != 'w':
            q.pop()
            b -= 1


for t in ret:
    print(t)
