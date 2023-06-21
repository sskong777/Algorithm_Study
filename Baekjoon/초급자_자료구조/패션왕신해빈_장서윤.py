t = int(input())

for i in range(t):
    cnt = 1
    c = dict()
    n = int(input())
    for j in range(n):
        v, k = input().split()
        if k in c.keys():
            c[k] += 1
        else:
            c[k] = 1

    for item in c.items():
        cnt *= item[1] + 1

    print(cnt-1)