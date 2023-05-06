a, b = map(int, input().split())

nums = [0]

for i in range(1, b+1):
    nums += [i]*i

print(sum(nums[a:b+1]))