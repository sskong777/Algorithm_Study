from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

l = [i for i in range(n, 0, -1)]
d = deque()
t = list(input().split())
t = t[::-1]
for i in t:
    if i == '1':
        d.append(l.pop())
    elif i == '2':
        d.insert(-1, l.pop())
    elif i == '3':
        d.appendleft(l.pop())
d.reverse()
d = map(str, d)

print(' '.join(d))