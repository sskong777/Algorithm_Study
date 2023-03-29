import sys
import math
input = sys.stdin.readline

a, d = map(int, input().split())
q = int(input())

for _ in range(q):
    c, l, r = map(int, input().split())
    answer = 0
    temp = a + ((l - 1) * d)
    n = r - l + 1
    if c == 1:
        answer = (n * ((2 * temp) + ((n - 1)*d))) // 2
    elif c == 2:
        if r == l:
            answer = temp
        else:
            answer = math.gcd(temp, d)
    print(answer)