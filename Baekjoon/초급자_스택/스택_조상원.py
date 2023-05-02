import sys
from collections import deque


input = sys.stdin.readline
n = int(input())

arr = [input().strip() for _ in range(n)]


# print(arr)
s = deque()

for c in arr:
    l = c.split()
    if len(l) > 1:
        # print(l)
        s.append(int(l[-1]))
    com = l[0]
    if com == 'top':
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
    elif com == 'empty':
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif com == 'size':
        print(len(s))
    elif com == 'pop':
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())