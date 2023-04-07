G = int(input())

c, b = 2, 1
check = False
while b <= 50000:
    if G == c * c - b * b:
        print(c)
        check = True
        c += 1
    elif G > c * c - b * b:
        c += 1
    else:
        b += 1

if not check:
    print(-1)
