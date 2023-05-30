from collections import deque

n = int(input())
dq = deque()

dq.append(n) # 마지막 수를 넣어두고,

for i in range(n-1, 0, -1):
    dq.appendleft(i) # 거꾸로 일단 추가시키기

    for j in range(i):
        move = dq.pop()
        dq.appendleft(move)

print(*dq)