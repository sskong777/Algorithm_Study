n = int(input())

for _ in range(n):
    clothes = {}
    k = int(input())

    for _ in range(k):
        name, kind = input().split()

        if kind not in clothes:
            clothes[kind] = []

        clothes[kind].append(name)

    count = 1
    for key in clothes:
        count *= len(clothes[key]) + 1

    print(count - 1)
