import sys

from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

d = deque([i for i in range(1, n+1)])

arr = list(map(int, input().split()))
cnt = 0
for i in arr:
    idx = d.index(i)
    while True:
        if i == d[0]:
            d.popleft()
            break
        if idx <= len(d)//2:
            while i != d[0]:
                d.rotate(-1)
                cnt+=1
        else:
            while i != d[0]:
                d.rotate(1)
                cnt+=1


print(cnt)