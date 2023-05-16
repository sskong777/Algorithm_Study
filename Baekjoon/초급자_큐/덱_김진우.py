import sys
from collections import deque
n = int(sys.stdin.readline())

deq = deque()

for _ in range(n):
    word = sys.stdin.readline().split()

    if word[0] == 'push_back':
        deq.append(word[1])
    elif word[0] == 'push_front':
        deq.appendleft(word[1])
    elif word[0] == 'pop_front':
        print(deq.popleft()) if deq else print('-1')
    elif word[0] == 'pop_back':
        print(deq.pop()) if deq else print('-1')
    elif word[0] == 'size':
        print(len(deq))
    elif word[0] == 'empty':
        print('0') if deq else print('1')
    elif word[0] == 'front':
        print(deq[0]) if deq else print('-1')
    elif word[0] == 'back':
        print(deq[-1]) if deq else print('-1')