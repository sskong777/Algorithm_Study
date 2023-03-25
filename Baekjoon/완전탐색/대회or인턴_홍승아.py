# [2875] 대회 or 인턴 (브론즈 3)
N, M, K = map(int, input().split())
cnt = 0
for n in range(N+1):
    for m in range(M+1):
        if n+m <= (N+M-K) and n == 2*m:
            cnt = max(cnt, m)

print(cnt)