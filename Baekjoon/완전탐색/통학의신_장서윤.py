A, B = map(int, input().split())

a = int(-A + (A**2-B)**0.5)
b = int(-A - (A**2-B)**0.5)

if a < b:
    print(a, b)
elif a == b:
    print(a)
else:
    print(b, a)