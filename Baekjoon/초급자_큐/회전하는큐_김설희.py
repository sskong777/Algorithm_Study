from collections import deque

n, m = map(int, input().split())
locations = list(map(int, input().split())) # 지민이가 뽑아내려고 하는 원소의 위치
dq = deque([i for i in range(1, n+1)])

cnt = 0
for i in locations:
    while True:
        if dq[0] == i: # 1번 연산 수행
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2: # 2번 연산 수행
                while dq[0] != i:
                    dq.append(dq.popleft())
                    cnt += 1
            else:
                while dq[0] != i: # 3번 연산 수행
                    dq.appendleft(dq.pop())
                    cnt += 1

print(cnt)

