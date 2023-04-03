a,b,n,w = list(map(int, input().split()))

p = list()

for i in range(1, n):
    x, y = i, n-i
    if a*x + b*y == w:
        p.append([x, y])


if 0 >= len(p) or len(p) >= 2:
    print(-1)
else:
    x, y = p.pop()
    print(x, y)

