M, N = map(int, input().split(' '))

if_ok = True

for i in range(M, N+1):
    if i == 1:
        continue

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            if_ok = False
            break
    if(if_ok == True):
        print(i)

    if_ok = True