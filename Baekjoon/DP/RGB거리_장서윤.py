N = int(input())

dp = [[0] * 3 for _ in range(1001)]
ans=list()

for i in range(1, N+1):
    cost = list(map(int, input().split()))

    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[2]

for i in range(3):
    ans.append(dp[N][i])

ans.sort()
print(ans[0])
