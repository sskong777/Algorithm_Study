from itertools import combinations
from math import lcm

nums = list(map(int, input().split()))
lcm3 = []

for comb in combinations(nums, 3):
    a, b, c = comb
    lcm2 = lcm(lcm(a, b), c)
    lcm3.append(lcm2)

print(min(lcm3))