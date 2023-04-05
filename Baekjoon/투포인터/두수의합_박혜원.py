# [3272] 두수의합

n = int(input())  # 수열의 크기, 데이터의 개수
data = list(map(int, input().split()))  # 전체 수열
m = int(input())  # 찾고자 하는 부분합 M
data.sort()

start, end = 0, n-1
count = 0


while start < end:
    interval_sum = data[start] + data[end]
    if interval_sum < m:
        start += 1
    elif interval_sum > m:
        end -= 1
    else:
        count += 1
        start += 1
print(count)


# 시도1(시간초과-완탐)
# input()
# num_list = list(map(int, input().split()))
# numnum = int(input())


# count = 0
# for i in num_list:
#     for j in num_list:
#         if i < j:
#             if i + j == numnum:
#                 count += 1
# print(count)
