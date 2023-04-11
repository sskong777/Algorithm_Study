# [1806] 부분합

"""
# 시도1 - 시간초과
매번 리스트의 일부분을 더해서 계산 하기 떄문
n, s = map(int, input().split())
num_list = list(map(int, input().split()))

start, end = 0, 1
check = True
answer = []
while start < end and end <= n:
    interval_sum = sum(num_list[start:end])
    if interval_sum < s:
        end += 1
    elif interval_sum > s:
        start += 1
    else:
        answer.append(len(num_list[start:end]))
        check = False
        print(min(answer))
        break

if check == True:
    print(0)
"""

n, s = map(int, input().split())
num_list = list(map(int, input().split()))

start, end = 0, 1
check = True
answer = []