import sys
from collections import deque
input = sys.stdin.readline

result=[]
n = int(input())
queue = deque()
state = 0  
b = 0
w = 0
for _ in range(n):
    i = input().rstrip()
    if i == "pop":
        if len(queue) != 0:
            e = queue.popleft()
            if e == 0:
                b -= 1
            elif e == 1:
                w -= 1
    else:
        cmd, opt = i.split()
        if cmd == "push":
            if opt == "b":
                queue.append(0)
                b += 1
            if opt == "w":
                queue.append(1)
                w += 1
        elif cmd == "rotate":
            if opt == "l":
                state -= 1
            elif opt == "r":
                state += 1
            if state == 4:
                state = 0
            elif state == -1:
                state = 3
        elif cmd == "count":
            if opt == "b":
                result.append(b)
            elif opt == "w":
                result.append(w)
    if state % 2 == 1:
        while (len(queue) != 0 and (queue[0 if state == 1 else len(queue) - 1]) != 1):
            if state == 1:
                queue.popleft()
            else:
                queue.pop()
            b -= 1

for i in result:
    print(i)