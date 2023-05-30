from collections import deque
import sys

input = sys.stdin.readline

n= int(input())

list_que=deque()
quest=[input() for _ in range(n)]
for i in quest:
    i=i.split()
    if i[0]=='push':
        list_que.append(i[1])
    elif i[0]=='pop':
        if list_que:
            print(list_que.popleft())
        else:
            
            print(-1)
    elif i[0]=='size':
        print(len(list_que))
    elif i[0]=='empty':
        if list_que:
            print(0)
        else:
            print(1)
            
    elif i[0]=='front':
        if list_que:
            print(list_que[0])
        else:
            print(-1)
    elif i[0]=='back':
        if list_que:
            print(list_que[-1])
        else:
            print(-1)