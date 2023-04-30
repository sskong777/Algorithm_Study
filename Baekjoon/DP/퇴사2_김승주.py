import sys
input = sys.stdin.readline

n = int(input())

arr = []
dp = [0] * (n+1)
for _ in range(n):
    arr.append(tuple(map(int, input().split())))

result = 0
for i in range(n):
    result = max(result, dp[i])
    t, p = arr[i]
    if i+t > n :
        continue
    else:
        dp[i+t] = max(dp[i+t], result+ p)

print(max(dp))



''' 
코드 2?!

import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
t, p = [0 for _ in range(n + 1)], [0 for _ in range(n + 1)]

dp = [0 for _ in range(n + 1)]
for i in range(1, n+1):
    t[i], p[i] = map(int, input().split())


for i in range(1, n+1):
    dp[i] = max(dp[i], dp[i - 1])  
    final_date = i+t[i]-1
    if i + t[i] -1 <=n :
        dp[i+t[i]-1]= max(dp[i+t[i]-1], dp[i-1]+p[i])
print(max(dp))

'''