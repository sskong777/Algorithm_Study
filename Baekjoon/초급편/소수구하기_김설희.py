m, n = map(int, input().split())
nums = [i for i in range(m, n + 1)]

for num in nums:
    if num == 1:
        continue

    # 해당 수의 제곱근까지의 약수를 구하면
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num)