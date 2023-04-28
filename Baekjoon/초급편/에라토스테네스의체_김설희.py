n, k = map(int, input().split())

# 2부터 N까지!

nums = [0]*(n + 1)

for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if nums[j] != 1:
            nums[j] = 1
            if sum(nums) == k:
                print(j)
                break