N = int(input())

top = list(map(int, input().split()))

ans = 0

for i in range(1, N):
    if top[i-1] <= top[i]:
        ans += 1

print(ans+1)
