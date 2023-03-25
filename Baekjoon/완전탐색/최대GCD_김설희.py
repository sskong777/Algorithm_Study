from math import gcd

n = int(input())

for _ in range(n):
    gcds = []
    nums = list(map(int, input().split()))

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            gcds.append(gcd(nums[i], nums[j]))

    print(max(gcds))
