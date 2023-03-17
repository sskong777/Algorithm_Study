a, b = map(int, input().split())
for i in range(-1001, 1001):
    for j in range(i, 1001):
        if i + j == (-2) * a and i*j == b:
            if i == j:
                print(i)
            else:
                print(i, j)