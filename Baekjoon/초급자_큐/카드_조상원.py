from collections import deque
n = int(input())

d = deque()

for i in range(n, 0, -1):
    d.appendleft(str(i))
    for j in range(i):
        d.appendleft(d.pop())

# print(d)
print(' '.join(d))
