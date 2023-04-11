# # 시도 1 - 시간 초과
# import sys
# input = sys.stdin.readline
# from itertools import permutations
#
# tc = int(input())
# for _ in range(tc):
#     n = int(input())
#     dots = list(map(int, input().strip().split()))
#     dots.sort()
#
#     cnt = 0
#     tmp_dots = list(map(list, permutations(dots, 2)))
#     for tmp in tmp_dots:
#         mid = (tmp[0] + tmp[1]) / 2
#         if mid == int(mid):
#             if mid in dots:
#                 cnt += 1
#     cnt //= 2
#     print(cnt)

# # 시도 2 - 이분 탐색
# import sys
# input = sys.stdin.readline
#
# def binary_search(left, right):
#     if (dots[left] + dots[right]) % 2 != 0:
#         return False
#     target = (dots[left] + dots[right]) // 2
#     visited = [False] * n
#     checking = left + right // 2
#     while left <= checking <= right and not visited[checking]:
#         if dots[checking] == target:
#             return True
#         elif dots[checking] < target:
#             visited[checking] = True
#             checking += 1
#         else:
#             visited[checking] = True
#             checking -= 1
#     return False
#
# tc = int(input())
# for _ in range(tc):
#     n = int(input())
#     dots = list(map(int, input().strip().split()))
#     dots.sort()
#
#     cnt = 0
#     for left in range(n-1):
#         for right in range(left+1, n):
#             # 이분 탐색
#             if binary_search(left, right):
#                 cnt += 1
#     print(cnt)


# 시도 3 - 처음 풀었던 풀이 - pypy3로만 변경
import sys
input = sys.stdin.readline


tc = int(input())
for _ in range(tc):
    n = int(input())
    dots = list(map(int, input().strip().split()))
    dots.sort()

    cnt = 0
    for left in range(n - 1):
        for right in range(left + 1, n):
            # 이분 탐색
            if (dots[left] + dots[right]) % 2 == 0 and (dots[left] + dots[right]) // 2 in dots:
                cnt += 1
    print(cnt)
