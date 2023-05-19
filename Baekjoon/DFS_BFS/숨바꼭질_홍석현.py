def bfs(N):
    v = [0] * 100001
    q = []
    q.append(N)
    v[N] = 1

    while q:
        now = q.pop(0)

        if now == K:
            return v[now]

        for i in now-1, now+1, now*2:
            if 0<=i<100001 and not v[i]:
                q.append(i)
                v[i] = v[now] + 1


N, K = map(int,input().split())                 # 5 17
ans = bfs(N)
print(ans-1)