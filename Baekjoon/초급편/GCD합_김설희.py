import math

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    n = nums[0]
    case = nums[1:]

    result = 0
    for i in range(len(case)):
        for j in range(i+1, len(case)):
            result += math.gcd(case[i], case[j])

    print(result)
