from collections import deque

def find_start():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                starts.append((i,j))

def bfs(starts):
    q = deque(starts)

    while q:
        ci,cj = q.popleft()
        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]==0:
                q.append((ni,nj))
                arr[ni][nj] = arr[ci][cj] + 1


M, N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

starts = []
find_start()
bfs(starts)

res = 0
for i in arr:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    res = max(res,max(i))
print(res-1)



