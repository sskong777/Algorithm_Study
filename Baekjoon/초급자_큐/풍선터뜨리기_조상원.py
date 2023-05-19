import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))
d = deque([(i, v) for i, v in enumerate(l)])
ret = []

while d:
    i, j = d.popleft()

    ret.append(str(i + 1))

    if j > 0:
        d.rotate(-j + 1)
    elif j < 0:
        d.rotate(-j)

print(' '.join(ret))
