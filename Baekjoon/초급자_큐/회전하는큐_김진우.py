from collections import deque

que = deque()

n, m = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(1,n+1):
    que.append(i)

cnt = 0

for i in arr:
    while True:
        if que[0] == i :
            que.popleft()
            break
        else:
            if que.index(i) <= len(que)//2:
               que.rotate(-1)
               cnt += 1
            else:
                que.rotate(1)
                cnt += 1

print(cnt)