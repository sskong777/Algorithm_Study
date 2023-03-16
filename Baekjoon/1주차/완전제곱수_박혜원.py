# 방법 1
num = int(input())
count = 0
for a in range(1, 501):
    for b in range(1, a+1):
        if num == a**2 - b**2:
            count += 1
print(count)


# 방법 2
num = int(input())
count = 0
for b in range(1, 501):
    for a in range(b, 501):
        if num == a**2 - b**2:
            count += 1
print(count)
