import sys
from collections import deque

N = int(input())

deq = deque()

for n in range(N):
    com = sys.stdin.readline().split()

    if com[0] == "push_front":
        deq.appendleft(com[1])

    elif com[0] == "push_back":
        deq.append(com[1])

    elif com[0] == "pop_front":
        if deq:
            print(deq[0])
            deq.popleft()
        else:
            print(-1)

    elif com[0] == "pop_back":
        if deq:
            print(deq[-1])
            deq.pop()
        else:
            print(-1)

    elif com[0] == "size":
        print(len(deq))

    elif com[0] == "empty":
        if deq:
            print(0)
        else:
            print(1)

    elif com[0] == "front":
        if deq:
            print(deq[0])
        else:
            print(-1)

    elif com[0] == "back":
        if deq:
            print(deq[-1])
        else:
            print(-1)