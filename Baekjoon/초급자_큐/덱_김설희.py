import sys
from collections import deque

n = int(sys.stdin.readline())

dq = deque()

for _ in range(n):
    word = sys.stdin.readline().split()

    if word[0] == 'push_back':
        dq.append(word[1])
    elif word[0] == 'push_front':
        dq.appendleft(word[1])
    elif word[0] == 'pop_front':
        print(dq.popleft()) if dq else print('-1')
    elif word[0] == 'pop_back':
        print(dq.pop()) if dq else print('-1')
    elif word[0] == 'size':
        print(len(dq))
    elif word[0] == 'empty':
        print('0') if dq else print('1')
    elif word[0] == 'front':
        print(dq[0]) if dq else print('-1')
    elif word[0] == 'back':
        print(dq[-1]) if dq else print('-1')