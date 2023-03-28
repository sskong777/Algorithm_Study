# [2869] 달팽이는올라가고싶다
# 달팽이가 첫날 정상까지 올라가니까 올라가는 횟수 = x, 내려오는 횟수 = x-1
# Ax + B(x-1) = v

import math
A, B, V = map(int, input().split())

x = (V-B) / (A-B)

print(math.ceil(x))  # 올림(ceil)
