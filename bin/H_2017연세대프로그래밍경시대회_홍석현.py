N = int(input())

ans = 0
for a in range(1,N-2):          # 영훈
    for b in range(a+2, N):     # 남규
        for c in range(2,N,2):  # 택희
            if a+b+c ==N:
                ans += 1

print(ans)