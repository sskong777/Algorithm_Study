# [1978]  소수 찾기
n = int(input())
nums = map(int, input().split())

count = 0
for num in nums:   # [ 1 3 5 7]
    for i in range(2, num+1):  # i = 2 3 4  (1은 소수가 아니므로 2부터)
        if num % i == 0:  # 1과 자기 자신이 아닌 수로 나누어지면 안됨
            if num == i:
                count += 1
            break


print(count)


# num = 3, i= 2, 3
# num = 5, i= 2, 3, 4, 5
# num = 7, i= 2, 3, 4, 5, 6, 7
