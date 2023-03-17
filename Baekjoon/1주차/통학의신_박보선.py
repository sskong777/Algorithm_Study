import sys
input = sys.stdin.readline


b, c = map(int, input().split())

r1 = int((-b + (((b**2) - c) ** (1/2))))
r2 = int((-b - (((b**2) - c) ** (1/2))))

if r1 == r2:
    print(r1)
else:
    print(*sorted([r1, r2]))