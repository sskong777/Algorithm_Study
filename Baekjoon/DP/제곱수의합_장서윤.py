N = int(input())


dp=[0 for _ in range(N+1)]
a = int(N**0.5)

for i in range(1, N+1):
    dp[i] = i

    for j in range(1, a+1):
        if j*j > i:
            break
        dp[i]= min(dp[i], dp[i-j*j]+1)


print(dp[N])

