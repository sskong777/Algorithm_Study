N,K = map(int,input().split())
arr = list(map(int,input().split()))
# print(arr)

ans = -1000
for i in range(N-K+1):
    ssum = sum(arr[i:i+K])
    ans = max(ans,ssum)

print(ans)