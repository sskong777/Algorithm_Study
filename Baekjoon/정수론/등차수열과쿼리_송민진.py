# # 시도 1
# import sys
# input = sys.stdin.readline
#
# a, d = map(int, input().strip().split())
# q = int(input())
#
# def calc_sum(left, right):
#     return (right - left + 1) * ((a + (left - 1) * d) + (a + (right - 1) * d)) // 2
#
# # 유클리드 호제법
# def calc_gcd(x, y):
#     while y > 0:
#         x, y = y, x % y
#     return x
#
# for _ in range(q):
#     type, left, right = map(int, input().strip().split())
#     answer = 0
#     if type == 1:
#         answer = calc_sum(left, right)
#     else:
#         start, end = a+(left-1)*d, a+(right-1)*d
#         gcd = start
#         for ai in range(start+d, end+1, d):
#             gcd = calc_gcd(gcd, ai)
#         answer = gcd
#
#     print(answer)

# 시도 2
import sys
import math
input = sys.stdin.readline

a, d = map(int, input().strip().split())
q = int(input())

def calc_sum(n, al, ar):
    return n * (al + ar) // 2

for _ in range(q):
    type, left, right = map(int, input().strip().split())
    n = right - left + 1
    al, ar = (a + (left - 1) * d), a + (right - 1) * d
    answer = -1
    if type == 1:
        answer = calc_sum(n, al, ar)
    else:
        if left == right:
            answer = al
        else:
            answer = math.gcd(al, d)
    print(answer)