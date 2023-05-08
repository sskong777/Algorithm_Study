import sys 
from collections import deque

input = sys.stdin.readline

n = int(input())
coms = [input() for _ in range(n)]
q = deque()

for com in coms:
    com = com.split()
    
    if len(com) >= 2:
        q.append(com[1])
    else:
        com = com[0]
        # print(com)
        if com == "pop":
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif com == "size":
            print(len(q))
        elif com == "empty":
            if len(q) == 0:
                print(1)
            else:
                print(0)
        elif com == "front":
            if q:
                print(q[0])
            else:
                print(-1)
        elif com == "back":
            if q:
                print(q[-1])
            else:
                print(-1)
        # print(com)