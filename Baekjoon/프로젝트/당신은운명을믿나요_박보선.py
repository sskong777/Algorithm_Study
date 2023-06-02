import sys
from collections import deque
input = sys.stdin.readline

k = deque(['K', 'O', 'R', 'E', 'A'])
y = deque(['Y','O','N','S','E','I'])

university = list(input().strip())

for u in university:
    if k[0] == u:
        k.popleft()
        if len(k) == 0:
            print('KOREA')
            break
    if y[0] == u:
        y.popleft()
        if len(y) == 0:
            print('YONSEI')
            break