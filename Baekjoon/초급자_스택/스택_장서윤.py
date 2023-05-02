import sys


N = int(sys.stdin.readline())


stack= [None for _ in range(100001)]

top = -1
size = 0

for n in range(N):
    com = sys.stdin.readline().split()

    if com[0] == "push":
        top+=1
        stack[top] = int(com[1])
        size +=1

    elif com[0] == "pop":
        if top != -1:
            print(stack[top])
            stack[top] = None
            top-=1
            size -=1
        else:
            print(-1)

    elif com[0] == "size":
        print(size)

    elif com[0] == "empty":
        if top == -1:
            print(1)
        else:
            print(0)

    elif com[0] == "top":
        if top != -1:
            print(stack[top])
        else:
            print(-1)
