import sys
input = sys.stdin.readline

n,k = map(int,input().split())
degrees = list(map(int,input().split()))

ans = -1e9
for i in range(n-k+1):
    sum = 0
    for j in range(k):
        sum += degrees[i+j]
    ans = max(ans,sum)
print(ans)