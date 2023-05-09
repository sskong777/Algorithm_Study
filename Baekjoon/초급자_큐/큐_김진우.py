import sys

input = sys.stdin.readline

n = int(input())

deque = []

for _ in range(n):
    a = input().split()
    if a[0] == 'push':
        deque.append(a[1])
    elif a[0] == 'pop':
        if deque:
            print(deque[0])
            deque.pop(0)
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(deque))
    elif a[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif a[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    else:
        if deque:
            print(deque[len(deque)-1])
        else:
            print(-1)