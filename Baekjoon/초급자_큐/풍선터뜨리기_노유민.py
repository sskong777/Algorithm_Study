from collections import deque
import sys

input = sys.stdin.readline

n=int(input())

l=list(map(int,input().split()))

q=deque( (i+1,v) for i,v in enumerate(l))


for i in range(n):
    now_index, next_location = q.popleft()
    print(now_index,end=" ")
    if next_location<0:
        q.rotate(-next_location)
    else:
        next_location-=1
        q.rotate(-next_location)