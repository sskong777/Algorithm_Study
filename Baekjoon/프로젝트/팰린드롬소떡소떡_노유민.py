from collections import deque

n = int(input())

li = list(input())

q = deque(li)

count = 0

while(True):
    if len(q) == 1 or len(q) == 0:
        break

    front = q.popleft()
    back = q.pop()
    if front != back:
        count += 1

print(count)
