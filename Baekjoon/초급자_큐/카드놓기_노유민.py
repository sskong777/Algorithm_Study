from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

l = list(map(int, input().split()))
l.reverse()

q = deque()

for i in range(n):
    if l[i] == 1:
        q.appendleft(i+1)
    elif l[i] == 2:
        q.insert(1, i+1)
    else:
        q.append(i+1)

for i in q:
    print(i, end=" ")