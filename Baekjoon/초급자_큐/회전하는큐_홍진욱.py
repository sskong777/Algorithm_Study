import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))

dq = deque()
for i in range(1, n+1):
    dq.append(i)

count = 0

for target in targets:
    if dq.index(target) <= len(dq) // 2:
        while dq[0] != target:
            dq.append(dq.popleft())
            count += 1
    else:
        while dq[0] != target:
            dq.appendleft(dq.pop())
            count += 1
    dq.popleft()

print(count)
