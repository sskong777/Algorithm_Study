import sys

from collections import deque

n = int(sys.stdin.readline())

que = deque()

direction = 0
b, w = 0, 0

for _ in range(n):
    comm = sys.stdin.readline().strip()

    if comm == "push b":
        que.appendleft("b")
        b += 1

    elif comm == "push w":
        que.appendleft("w")
        w += 1

    elif comm == "pop":
        if que:
            v = que.pop()
            if v == "b":
                b -= 1
            else:
                w -= 1

    elif comm == "rotate l":
        direction = (direction - 1) % 4

    elif comm == "rotate r":
        direction = (direction + 1) % 4

    elif comm == "count b":
        print(b)

    elif comm == "count w":
        print(w)

    if direction == 1 or direction == -3:
        while que:
            if que[-1] == "w":
                break
            que.pop()
            b -= 1

    elif direction == 3 or direction == -1:
        while que:
            if que[0] == "w":
                break
            que.popleft()
            b -= 1
