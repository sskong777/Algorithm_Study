import sys

from collections import deque

input = sys.stdin.readline

n = int(input())

commands = [input() for _ in range(n)]
# print(commands)
d = deque([])

for com in commands:
    com = com.split()
    # print(com)
    if len(com) > 1:
        if com[0] == "push_back":
            d.append(int(com[1]))
        elif com[0] == "push_front":
            d.appendleft(int(com[1]))
    else:
        com = com[0]
        if com == "pop_front":
            if len(d) == 0:
                print(-1)
            else:
                print(d.popleft())
        elif com == "pop_back":
            if len(d) == 0:
                print(-1)
            else:
                print(d.pop())
        elif com == "size":
            print(len(d))
        elif com == "empty":
            if len(d) == 0:
                print(1)
            else:
                print(0)
        elif com == "front":
            if len(d) ==0:
                print(-1)
            else:
                print(d[0])
        elif com == "back":
            if len(d) == 0:
                print(-1)
            else:
                print(d[-1])