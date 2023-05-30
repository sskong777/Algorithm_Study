# [2164] 카드2
from collections import deque

n = int(input())  # 6
queue = deque()  # [1,2,3,4,5,6]

for i in range(1, n+1):
    queue.append(i)

while len(queue) > 1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue[0])
