from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int,input().split())

q= deque(list(i+1 for i in range(n)))

list_index = list(map(int,input().split()))

count = 0
for i in list_index:
    location=q.index(i)

    if location==0:
        q.popleft()
        continue
    if location<=(len(q)//2):
        q.rotate(-(location))
        q.popleft()
        count+=location
    else:
        q.rotate(len(q)-location)
        q.popleft()
        count+=(len(q)-location+1)

print(count)