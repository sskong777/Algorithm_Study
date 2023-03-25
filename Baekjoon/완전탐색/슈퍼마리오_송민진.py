sum = 0
for _ in range(10):
    tmp = sum + int(input())
    if abs(100 - sum) < abs(100-tmp):
        break
    sum = tmp

print(sum)