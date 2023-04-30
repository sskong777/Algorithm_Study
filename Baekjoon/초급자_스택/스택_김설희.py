import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    word = sys.stdin.readline().split()

    if word[0] == 'push':
        stack.append(word[1])
    elif word[0] == 'pop':
        print(stack.pop()) if len(stack) != 0 else print(-1)
    elif word[0] == 'size':
        print(len(stack))
    elif word[0] == 'empty':
        print(1) if len(stack) == 0 else print(0)
    elif word[0] == 'top':
        print(stack[-1]) if len(stack) != 0 else print(-1)