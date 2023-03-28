n = int(input())
cnt = 0
for b in range(1, 501):
    a = (b**2 + n)**(1/2)
    if 1 <= a <= 500 and int(a) == a:
        cnt += 1

print(cnt)