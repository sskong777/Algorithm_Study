n = int(input())

cnt = 0

for i in range(1,501):
    for j in range(1,501):
        a,b = i,j
        if a**2 == b**2 + n:
            cnt += 1

print(cnt)