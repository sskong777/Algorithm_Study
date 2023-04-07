# [2003] 수들의 합
n, m = map(int, input().split())  # 데이터의 개수, 부분합 M
data = list(map(int, input().split()))  # 전체 수열


start, end = 0, 1
count = 0


while start <= end and end <= n:
    interval_sum = sum(data[start:end])
    if interval_sum < m:
        end += 1
    elif interval_sum > m:
        start += 1
    else:
        count += 1
        end += 1

print(count)
