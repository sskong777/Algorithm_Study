n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

ans = 0
for i in range(n):
    a = A[i]
    b = max(B)

    B.pop(B.index(b))

    ans += a*b

print(ans)