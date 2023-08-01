from pprint import pprint

N, K = map(int, input().split())

w = [0] * (N+1)
v = [0] * (N+1)

for i in range(1, N+1):
    w[i], v[i] = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]

pprint(dp)
print(dp[N][K])