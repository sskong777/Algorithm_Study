def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
t = int(input())

for _ in range(t):
    n, *nums = map(int, input().split())
    gcd_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            gcd_sum += gcd(nums[i], nums[j])
    print(gcd_sum)