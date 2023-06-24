def bfs(si,sj):
    mmax = 0
    q = []
    q.append((si,sj))
    visited = [[0] * M for _ in range(N)]
    visited[si][sj] = 1


    while q:
        ci,cj = q.pop(0)

        for di,dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] == 'L':
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
                mmax = max(mmax, visited[ni][nj])
    return mmax-1


N, M = map(int,input().split())

arr = [list(input()) for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            v = bfs(i,j)
            ans = max(ans,v)
print(ans)