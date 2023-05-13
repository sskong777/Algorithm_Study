import sys
from collections import deque

input = sys.stdin.readline

total = int(input())
ret = []
for _ in range(total):
    n, i = map(int, input().split())
    q = list(map(int, input().split()))
    q = deque([(v, idx) for idx, v in enumerate(q)])
    count = 0
    while True:
        if max(q)[0] == q[0][0]:
            check = q.popleft()
            count += 1
            if check[1] == i:
                # print(count)
                ret.append(count)
                break
        else:
            q.append(q.popleft())

for v in ret:
    print(v)
