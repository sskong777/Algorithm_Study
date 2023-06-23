from collections import defaultdict
t = int(input())

for i in range(t):
    d = defaultdict(list)
    k = int(input())

    for _ in range(k):
        c, l = input().split()
        d[l].append(c)

    ret = 1
    for n in d:
        ret *= len(d[n]) + 1
    print(ret - 1)
