# [10824] 네수


# 시도 1 (실패)
"""
A, B, C, D = map(int, input().split())

length_B = 0
while B > 0:
    B //= 10
    length_B += 1
print(length_B)

length_D = 0
while D > 0:
    D //= 10
    length_D += 1
print(length_D)

print((A * 10**length_B) + B)
"""

# 시도 2 (int형 대신 string으로 받기)

A, B, C, D = input().split()

first = A + B
second = C + D
print(int(first) + int(second))
