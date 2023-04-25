import sys
input = sys.stdin.readline

n = int(input())

s = []
dp = [0 for _ in range(n + 1)]

for i in range(n):
    t, p = map(int, input().split())
    s.append([t, p])

for i in range(n - 1, -1, -1):
    t, p = s[i]
    
    if i + t > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], dp[i + t] + p)

print(dp[0])