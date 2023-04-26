import sys
import math
from itertools import combinations
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    arr = list(map(int, input().strip().split()))
    arr = arr[1:]
    gcds = []
    coms = list(combinations(arr, 2))
    for com in coms:
        gcd = math.gcd(com[0], com[1])
        gcds.append(gcd)

    answer = 0
    for g in gcds:
        answer += g

    print(answer)