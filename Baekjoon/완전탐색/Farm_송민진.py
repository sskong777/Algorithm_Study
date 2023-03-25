a, b, n, w = map(int, input().split())
sheep, goat = -1, -1

for s in range(1, n):
    if (w - (s * a)) % b == 0 and (w - (s * a)) / b == n - s:
        if sheep == -1:
            sheep = s
            goat = n - s
        else:
            sheep = -1
            break

if sheep == -1:
    print(-1)
else:
    print(sheep, goat)