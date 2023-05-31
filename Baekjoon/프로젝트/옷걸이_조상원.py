import sys
from collections import Counter

input = sys.stdin.readline

t = map(int, input().split())

arr = list(map(int, input().split()))
u, d = map(int, input().split())

c = Counter(arr)

u -= c[1]
d -= c[2]
ret = []
if u + d > c[3] or (u < 0 or d < 0):
    print('NO')
else:
    for i in arr:
        if i == 1:
            ret.append('U')
        elif i == 2:
            ret.append('D')
        else:
            if u > 0:
                ret.append('U')
                u -= 1
            elif d > 0:
                ret.append('D')
                d -= 1
    print('YES')
    print(''.join(ret))
