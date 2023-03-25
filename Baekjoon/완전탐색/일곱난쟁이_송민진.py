import itertools
nanjaengs = []

for _ in range(9):
    nanjaengs.append(int(input()))

for it in itertools.combinations(nanjaengs, 7):
    if sum(list(it)) == 100:
        print(*sorted(list(it)), end=" ")
        break