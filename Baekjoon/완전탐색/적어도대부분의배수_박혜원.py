# [1145] 적어도대부분의배수
nums = list(map(int, input().split()))

i = 0
while True:
    i += 1
    count = 0
    for num in nums:
        if i % num == 0:
            count += 1
    if count >= 3:
        print(i)
        break
