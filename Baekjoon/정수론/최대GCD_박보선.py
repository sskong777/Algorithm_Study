import sys
import math
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    nums = list(map(int, input().split()))
    answer = 0
    l = len(nums)
    for i in range(l - 1):
        for j in range(i + 1, l):
            answer = max(answer, math.gcd(nums[i], nums[j]))
    
    print(answer)