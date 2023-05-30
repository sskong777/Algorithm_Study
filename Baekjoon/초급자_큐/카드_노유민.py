from collections import deque

n = int(input())

q = deque()

for i in range(n, 0, -1):
    q.appendleft(str(i))
    for j in range(i):
        q.appendleft(q.pop())

print(" ".join(q))
