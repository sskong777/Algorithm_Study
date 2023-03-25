N = int(input())
ans = 0
for t in range(2,N-1, 2):
        ans += (N-t-2)//2
print(ans)
