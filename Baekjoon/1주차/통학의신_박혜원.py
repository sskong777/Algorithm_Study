import math
a, b = map(int, input().split())

# a = 1
# b = 1
# 근의 제곱 구기
# x1 = (-2*a + ((2*a)**2 - 4*b)**0.5) / 2
# x2 = (-2*a - ((2*a)**2 - 4*b)**0.5) / 2

x1 = -a - math.sqrt(a**2 - b)
x2 = -a + math.sqrt(a**2 - b)

if x1 == x2:
    print(int(x1))
else:
    print(int(x1), int(x2))
