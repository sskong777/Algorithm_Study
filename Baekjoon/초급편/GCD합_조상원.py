import sys
import math
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for l in arr:
    total = 0
    for i in range(1, len(l)):
        for j in range(1, len(l)):
            if i < j:
                total += math.gcd(l[i], l[j])

    print(total)
