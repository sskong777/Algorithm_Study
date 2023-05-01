import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    inputs = list(input().strip().split())
    command = inputs[0]
    if command == "push":
        num = int(inputs[1])
        stack.append(num)
    if command == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
    if command == "size":
        print(len(stack))
    if command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    if command == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
