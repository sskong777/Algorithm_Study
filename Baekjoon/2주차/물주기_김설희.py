n, k, a, b = map(int, input().split())

pots = [k]*n

day = 0
while True:
    if 0 in pots:
            break

    day += 1
    for i in range(a):
        pots[i] += b
    for i in range(n):
        pots[i] -= 1

    pots.sort()


print(day)