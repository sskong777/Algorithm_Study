n, k = map(int, input().split())
c = 0
erased = [0] * (n+1)


for i in range(2, n+1):
    if erased[i] == 0:
        for j in range(i, n+1, i):
            if erased[j] == 0:
                if c == k-1:
                    print(j)

                erased[j] = 1
                c += 1
