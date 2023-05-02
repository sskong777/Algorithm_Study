import sys
input = sys.stdin.readline

stack = []

n = int(input())

for _ in range(n):
    m = input().split()
    if m[0] == 'push':
        stack.append(m[1])
        # n -=1
    elif m[0] == 'pop':
        if len(stack) != 0 :
            print(stack[len(stack)-1])
            stack.pop(len(stack)-1)
            #  n -= 1
        else:
            print(-1)
            #  n -=1
    elif m[0] == 'size' :
        print(len(stack))
        #  n -= 1
    elif m[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
            #   n -= 1
        else:
            print(0)
            #   n -= 1
    else:
        if len(stack) != 0 :
            print(stack[len(stack)-1])
            #  n -= 1
        else:
            print(-1)
            #   n -= 1