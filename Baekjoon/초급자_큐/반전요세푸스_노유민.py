import sys
from collections import deque

input = sys.stdin.readline

n, k, m = map(int, input().split())

q = [i+1 for i in range(n)]

q = deque(q)

i = 0
while len(q) > 0:
    if i % m == 0 and i!=0:
        q.reverse()
    if len(q) == 1:
        print(q.popleft())
        break
    q.rotate(-(k-1))
    print(q.popleft())
    i += 1
