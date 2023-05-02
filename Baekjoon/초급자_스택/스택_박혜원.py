# [10828] 스택

import sys
n = int(sys.stdin.readline())

stack = []

for i in range(n):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "top":
        if len(stack) == 0:  # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력
            print(-1)
        else:   # 스택의 가장 위에 있는 정수를 출력
            print(stack[-1])
    elif command[0] == "size":  # 스택에 들어있는 정수의 개수를 출력
        print(len(stack))
    elif command[0] == "empty":   # 스택이 비어있으면 1, 아니면 0을 출력한다.
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "pop":
        if len(stack) == 0:  # 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
            print(-1)
        else:
            print(stack.pop())  # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다.
