import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    nums = list(map(int, input().strip().split()))
    max_gcd = 1
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                for gcd in range(1, min(nums[i], nums[j])+1):
                    if nums[i] % gcd == 0 and nums[j] % gcd == 0:
                        max_gcd = max(max_gcd, gcd)
    print(max_gcd)